from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.database import Base, engine
from controllers import usuario_controller, categoria_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PDV AAPM")

app.include_router(usuario_controller.router)
app.include_router(categoria_controller.router)

# Arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates (apontando para a pasta correta)
templates = Jinja2Templates(directory="app/templates")

# Rota da página inicial (usa o index.html)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rota da tela de login
@app.get("/login", response_class=HTMLResponse)
async def tela_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Rota do dashboard (protegido depois)
@app.get("/dashboard", response_class=HTMLResponse)
async def tela_dashboard(request: Request):
    usuario_logado = {"nome": "Jackelyne", "role": "ADMIN"}  # mock
    return templates.TemplateResponse("dashboard.html", {"request": request, "usuario": usuario_logado})

# Rota de visão geral
@app.get("/visualizacao", response_class=HTMLResponse)
async def tela_visualizacao(request: Request):   # ← atenção ao "def"
    return templates.TemplateResponse("visualizacao.html", {"request": request})