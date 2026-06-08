from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.categoria import Categoria



router = APIRouter(prefix="/categorias", tags=["Categorias"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# criar categoria
@router.post("/")
def criar_categoria(nome: str, db: Session = Depends(get_db)):
    categoria = Categoria(nome=nome)
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria

# listar categorias
@router.get("/")
def listar_categorias(db: Session = Depends(get_db)):
    return db.query(Categoria).all()
