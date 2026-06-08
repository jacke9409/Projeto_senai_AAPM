from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.usuario import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# conexão com banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# criar usuário
@router.post("/")
def criar_usuario(nome: str, email: str, senha: str, categoria_id: int, db: Session = Depends(get_db)):
    usuario = Usuario(
        nome=nome,
        email=email,
        senha=senha,
        categoria_id=categoria_id
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

# listar usuários
@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()