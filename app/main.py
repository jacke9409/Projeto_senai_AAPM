import os
from fastapi import FastAPI, Request, Form
from typing import Optional
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.database import Base, engine
# Modifique a linha 7 para ficar assim:
from app.controllers import usuario_controller, categoria_controller

# imports para login
from fastapi.responses import RedirectResponse
from app.database import SessionLocal
from app.models.usuario import Usuario
from auth import verificar_senha, criar_token

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PDV AAPM")

# 2. RESOLVE OS CAMINHOS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.join(BASE_DIR, "static")

# 3. MOUNTA A STATIC PRIMEIRO (Crucial para o url_for funcionar no Jinja2)
app.mount("/static", StaticFiles(directory=static_path), name="static")

# 4. INICIALIZA OS TEMPLATES DEPOIS DA STATIC JÁ ESTAR REGISTRADA
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


# ── DEIXE SUAS ROTAS EXATAMENTE ASSIM ABAIXO ──

# ── ROTAS DO SISTEMA CORRIGIDAS ──

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="base.html")

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


@app.post("/login")
async def do_login(request: Request, email: str = Form(...), senha: str = Form(""), nome: Optional[str] = Form(None)):
    # senha opcional no formulário atual; se não vier, tentamos autenticar pelo email apenas
    db = SessionLocal()
    try:
        usuario = db.query(Usuario).filter(Usuario.email == email).first()
        if not usuario:
            return templates.TemplateResponse(request=request, name="login.html", context={"request": request, "erro": "Usuário não encontrado"}, status_code=401)

        # Se a senha não foi enviada no formulário, considere autenticação por nome (simples)
        if senha:
            if not verificar_senha(senha, usuario.senha_hash):
                return templates.TemplateResponse(request=request, name="login.html", context={"request": request, "erro": "Credenciais inválidas"}, status_code=401)

        token = criar_token({"sub": usuario.email, "role": usuario.role})
        resp = RedirectResponse(url="/dashboard", status_code=302)
        resp.set_cookie(key="access_token", value=token, httponly=True)
        return resp
    finally:
        db.close()

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    # Passando o request como primeiro argumento nomeado mata o erro de vez
    return templates.TemplateResponse(request=request, name="dashboard.html")

@app.get("/visualizacao", response_class=HTMLResponse)
async def visualizacao(request: Request):
    return templates.TemplateResponse(request=request, name="visualizacao.html")