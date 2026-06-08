import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# 1. CRIA O APP (Apenas uma vez!)
app = FastAPI(title="Projeto SENAI AAPM")

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

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    # Passando o request como primeiro argumento nomeado mata o erro de vez
    return templates.TemplateResponse(request=request, name="dashboard.html")

@app.get("/visualizacao", response_class=HTMLResponse)
async def visualizacao(request: Request):
    return templates.TemplateResponse(request=request, name="visualizacao.html")