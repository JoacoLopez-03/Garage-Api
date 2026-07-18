from pydantic import BaseModel


class ModeloBase(BaseModel):
    nombre: str
    marca_id: int


class ModeloOut(ModeloBase):
    id: int

    class Config:
        from_attributes = True