from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.models.modelo import Modelo
from app.schemas.modelo import ModeloOut

router = APIRouter(prefix="/modelos", tags=["Modelos"])


@router.get("/", response_model=List[ModeloOut])
def listar_modelos(marca_id: Optional[int] = Query(None), db: Session = Depends(get_db)):
    query = db.query(Modelo)
    if marca_id:
        query = query.filter(Modelo.marca_id == marca_id)
    return query.all()