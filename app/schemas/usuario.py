from pydantic import BaseModel, EmailStr


class UsuarioBase(BaseModel):
    email: EmailStr
    nombre: str
    apellido: str


class UsuarioCreate(UsuarioBase):
    password: str


class UsuarioOut(UsuarioBase):
    id: int
    es_activo: bool

    class Config:
        from_attributes = True