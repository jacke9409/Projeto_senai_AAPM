from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal
from models.usuario import Usuario

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/api/login")
async def login(request: Request, email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.email == email).first()
    # comparação simples: se o projeto armazenou senha em texto ou em senha_hash
    senha_stored = getattr(user, "senha_hash", None) if user else None
    senha_alt = getattr(user, "senha", None) if user else None

    if not user or (senha_stored != senha and senha_alt != senha):
        return templates.TemplateResponse("auth/login.html", {"request": request, "error": "Credenciais inválidas"})

    response = RedirectResponse(url="/dashboard", status_code=303)
    return response
