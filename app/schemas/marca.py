from pydantic import BaseModel


class MarcaBase(BaseModel):
    nombre: str


class MarcaOut(MarcaBase):
    id: int

    class Config:
        from_attributes = True