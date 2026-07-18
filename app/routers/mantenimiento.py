from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.mantenimiento import Mantenimiento
from app.models.usuario import Usuario
from app.schemas.mantenimiento import MantenimientoCreate, MantenimientoOut
from app.core.dependencies import get_current_user
from app.services.vehiculo_service import obtener_vehiculo_propio
from app.services.mantenimiento_service import obtener_mantenimiento_por_vehiculo

router = APIRouter(prefix="/vehiculos/{vehiculo_id}/mantenimientos", tags=["Mantenimientos"])


@router.post("/", response_model=MantenimientoOut, status_code=status.HTTP_201_CREATED)
def crear_mantenimiento(
    vehiculo_id: int,
    mantenimiento_data: MantenimientoCreate,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(get_current_user),
):
    obtener_vehiculo_propio(vehiculo_id, usuario_actual, db)

    nuevo_mantenimiento = Mantenimiento(
        **mantenimiento_data.model_dump(),
        vehiculo_id=vehiculo_id,
    )

    db.add(nuevo_mantenimiento)
    db.commit()
    db.refresh(nuevo_mantenimiento)

    return nuevo_mantenimiento


@router.get("/", response_model=List[MantenimientoOut])
def listar_mantenimientos(
    vehiculo_id: int,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(get_current_user),
):
    obtener_vehiculo_propio(vehiculo_id, usuario_actual, db)
    
    return (
        db.query(Mantenimiento)
        .filter(Mantenimiento.vehiculo_id == vehiculo_id)
        .order_by(Mantenimiento.fecha.desc())
        .all()
    )

@router.get("/{mantenimiento_id}", response_model=MantenimientoOut)
def obtener_mantenimiento(
    vehiculo_id: int,
    mantenimiento_id: int,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(get_current_user),
):
    obtener_vehiculo_propio(vehiculo_id, usuario_actual, db)
    mantenimiento = obtener_mantenimiento_por_vehiculo(mantenimiento_id= mantenimiento_id, vehiculo_id= vehiculo_id, db=db)

    return mantenimiento


@router.put("/{mantenimiento_id}", response_model=MantenimientoOut)
def actualizar_mantenimiento(
    vehiculo_id: int,
    mantenimiento_id: int,
    mantenimiento_data: MantenimientoCreate,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(get_current_user),
):
    obtener_vehiculo_propio(vehiculo_id, usuario_actual, db)
    mantenimiento = obtener_mantenimiento_por_vehiculo(mantenimiento_id= mantenimiento_id, vehiculo_id= vehiculo_id, db=db)

    for campo, valor in mantenimiento_data.model_dump().items():
        setattr(mantenimiento, campo, valor)

    db.commit()
    db.refresh(mantenimiento)

    return mantenimiento


@router.delete("/{mantenimiento_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_mantenimiento(
    vehiculo_id: int,
    mantenimiento_id: int,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(get_current_user),
):
    obtener_vehiculo_propio(vehiculo_id, usuario_actual, db)
    mantenimiento = obtener_mantenimiento_por_vehiculo(mantenimiento_id= mantenimiento_id, vehiculo_id= vehiculo_id, db=db)

    db.delete(mantenimiento)
    db.commit()
    return None