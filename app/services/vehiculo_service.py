from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.vehiculo import Vehiculo
from app.models.usuario import Usuario


def obtener_vehiculo_propio(vehiculo_id: int, usuario_actual: Usuario, db: Session) -> Vehiculo:
    vehiculo = db.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()

    if not vehiculo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehículo no encontrado")

    if vehiculo.usuario_id != usuario_actual.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tenés permiso sobre este vehículo")

    return vehiculo