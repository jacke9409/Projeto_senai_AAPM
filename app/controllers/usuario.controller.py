from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.usuario import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# conexão com banco
db = SessionLocal()

# criar usuário
@router.post("/")
def criar_usuario(nome: str, email: str, senha: str, categoria_id: int):
    u = Usuario(
        nome=nome,
        email=email,
        senha=senha,
        categoria_id=categoria_id
    )
    db.add(u)
    db.commit()
    print("Usuário criado:", u.email)
    return u

# listar usuários
@router.get("/")
def listar_usuarios():
    return db.query(Usuario).all()