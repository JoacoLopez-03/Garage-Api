from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.vehiculo import Vehiculo
from app.models.usuario import Usuario
from app.schemas.vehiculos import VehiculoCreate, VehiculoOut
from app.core.dependencies import get_current_user
from app.services.vehiculo_service import obtener_vehiculo_propio

router = APIRouter(prefix="/vehiculos", tags=["Vehiculos"])


@router.post("/", response_model=VehiculoOut, status_code=status.HTTP_201_CREATED)
def crear_vehiculo(
    vehiculo_data: VehiculoCreate,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(get_current_user),
):
    patente_existente = db.query(Vehiculo).filter(Vehiculo.patente == vehiculo_data.patente).first()
    if patente_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un vehículo con esa patente",
        )

    nuevo_vehiculo = Vehiculo(
        **vehiculo_data.model_dump(),
        usuario_id=usuario_actual.id,
    )

    db.add(nuevo_vehiculo)
    db.commit()
    db.refresh(nuevo_vehiculo)

    return nuevo_vehiculo


@router.get("/", response_model=List[VehiculoOut])
def listar_mis_vehiculos(
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(get_current_user),
):
    return db.query(Vehiculo).filter(Vehiculo.usuario_id == usuario_actual.id).all()


@router.get("/{vehiculo_id}", response_model=VehiculoOut)
def obtener_vehiculo(
    vehiculo_id: int,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(get_current_user),
):
    return obtener_vehiculo_propio(vehiculo_id, usuario_actual, db)


@router.put("/{vehiculo_id}", response_model=VehiculoOut)
def actualizar_vehiculo(
    vehiculo_id: int,
    vehiculo_data: VehiculoCreate,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(get_current_user),
):
    vehiculo = obtener_vehiculo_propio(vehiculo_id, usuario_actual, db)

    for campo, valor in vehiculo_data.model_dump().items():
        setattr(vehiculo, campo, valor)

    db.commit()
    db.refresh(vehiculo)

    return vehiculo


@router.delete("/{vehiculo_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_vehiculo(
    vehiculo_id: int,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(get_current_user),
):
    vehiculo = obtener_vehiculo_propio(vehiculo_id, usuario_actual, db)
    db.delete(vehiculo)
    db.commit()
    return None