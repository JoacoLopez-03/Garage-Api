from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True)
    modelo_id = Column(Integer, ForeignKey("modelos.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    anio = Column(Integer, nullable=False)
    patente = Column(String, unique=True, index=True, nullable=False)
    kilometraje = Column(Integer, default=0)
    creado_en = Column(DateTime(timezone=True), server_default=func.now())

    modelo = relationship("Modelo", back_populates="vehiculos")
    propietario = relationship("Usuario", back_populates="vehiculos")
    mantenimientos = relationship("Mantenimiento", back_populates="vehiculo")