from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.marca import Marca
from app.schemas.marca import MarcaOut

router = APIRouter(prefix="/marcas", tags=["Marcas"])


@router.get("/", response_model=List[MarcaOut])
def listar_marcas(db: Session = Depends(get_db)):
    return db.query(Marca).all()