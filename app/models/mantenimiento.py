import enum
from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import relationship
from app.database import Base


class TipoMantenimiento(str, enum.Enum):
    CAMBIO_ACEITE = "cambio_aceite"
    DISTRIBUCION = "distribucion"
    NEUMATICOS = "neumaticos"
    FRENOS = "frenos"
    BATERIA = "bateria"
    SERVICE_GENERAL = "service_general"
    OTRO = "otro"


class Mantenimiento(Base):
    __tablename__ = "mantenimientos"

    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"), nullable=False)
    tipo = Column(SqlEnum(TipoMantenimiento), nullable=False)
    descripcion = Column(String, nullable=True)
    fecha = Column(Date, nullable=False)
    kilometraje = Column(Integer, nullable=False)
    costo = Column(Numeric(10, 2), nullable=True)

    vehiculo = relationship("Vehiculo", back_populates="mantenimientos")