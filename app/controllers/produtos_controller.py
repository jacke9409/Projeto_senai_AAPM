from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from database import get_db
from app.models.produto import Produto

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.get("/")
async def listar_produtos(request: Request, db: Session = Depends(get_db)):
    produtos = db.query(Produto).all()
    return {"produtos": produtos}  # depois trocar por template