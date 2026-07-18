from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.mantenimiento import Mantenimiento

def obtener_mantenimiento_por_vehiculo(mantenimiento_id: int, vehiculo_id: int, db: Session) -> Mantenimiento:
    mantenimiento = (
        db.query(Mantenimiento)
        .filter(Mantenimiento.id == mantenimiento_id, Mantenimiento.vehiculo_id == vehiculo_id)
        .first()
    )
    
    if not mantenimiento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mantenimiento no encontrado")
    
    return mantenimiento