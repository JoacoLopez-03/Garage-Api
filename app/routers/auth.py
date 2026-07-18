from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import verify_password, crear_access_token
from app.core.dependencies import get_current_user

from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioOut
from app.core.security import hash_password

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/registro", response_model=UsuarioOut, status_code=status.HTTP_201_CREATED)
def registro(usuario_data: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(Usuario).filter(Usuario.email == usuario_data.email).first()
    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un usuario con ese email"
        )

    nuevo_usuario = Usuario(
        email=usuario_data.email,
        nombre=usuario_data.nombre,
        apellido=usuario_data.apellido,
        hashed_password=hash_password(usuario_data.password),
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == form_data.username).first()

    if not usuario or not verify_password(form_data.password, usuario.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = crear_access_token(data={"sub": usuario.email})

    return {"access_token": access_token, "token_type": "bearer"}

from app.core.dependencies import get_current_user

@router.get("/me", response_model=UsuarioOut)
def leer_usuario_actual(usuario_actual: Usuario = Depends(get_current_user)):
    return usuario_actual