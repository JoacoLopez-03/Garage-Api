from datetime import date
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel
from app.models.mantenimiento import TipoMantenimiento


class MantenimientoBase(BaseModel):
    tipo: TipoMantenimiento
    descripcion: Optional[str] = None
    fecha: date
    kilometraje: int
    costo: Optional[Decimal] = None


class MantenimientoCreate(MantenimientoBase):
    pass


class MantenimientoOut(MantenimientoBase):
    id: int
    vehiculo_id: int

    class Config:
        from_attributes = True