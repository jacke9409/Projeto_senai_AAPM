import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Inicializa o FastAPI
app = FastAPI(title="Projeto SENAI AAPM")

# Descobre o caminho correto das pastas dentro de 'app'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configura os Templates e os Arquivos Estáticos com segurança
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Monta a pasta de arquivos estáticos (CSS, Imagens, SVGs)
static_path = os.path.join(BASE_DIR, "static")
if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")


# ── ROTAS DO SISTEMA ──

# 1. Rota Raiz (Página Inicial da AAPM - Base)
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="base.html")


# 2. Rota de Login (Index do fluxo de autenticação)
@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


# 3. Rota do Dashboard (Acessado após o login)
@app.get("/dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


# 4. Rota de Visualização (Catálogo de Estoque)
@app.get("/visualizacao")
async def visualizacao(request: Request):
    return templates.TemplateResponse(request=request, name="visualizacao.html")