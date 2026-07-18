from datetime import datetime
from pydantic import BaseModel


class VehiculoBase(BaseModel):
    modelo_id: int
    anio: int
    patente: str
    kilometraje: int = 0


class VehiculoCreate(VehiculoBase):
    pass


class VehiculoOut(VehiculoBase):
    id: int
    usuario_id: int
    creado_en: datetime

    class Config:
        from_attributes = True