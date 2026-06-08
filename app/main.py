from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Static
static_dir = os.path.join(BASE_DIR, "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Templates
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

def render(template_name: str, request: Request, extra_context: dict = None):
    context = {"request": request}
    if extra_context:
        context.update(extra_context)
    return templates.TemplateResponse(request=request, name=template_name, context=context)

# --- ROTAS PÚBLICAS ---

@app.get("/", response_class=HTMLResponse)
def pagina_login(request: Request):
    return render("index.html", request)

@app.get("/visualizacao", response_class=HTMLResponse)
def pagina_visualizacao(request: Request):
    return render("visualizacao.html", request)

# --- ROTA DE LOGIN (POST) ---

@app.post("/auth/login")
async def fazer_login(
    request: Request,
    username: str = Form(...),
    senha: str = Form(...)
):
    # 🔐 Substitua pela sua validação real
    if username == "admin@aapm.com" and senha == "123456":
        response = RedirectResponse(url="/dashboard", status_code=303)
        return response
    else:
        return render("index.html", request, {"erro": "E-mail ou senha inválidos"})

# --- ROTA DO DASHBOARD (PROTEGIDA) ---

@app.get("/dashboard", response_class=HTMLResponse)
def pagina_dashboard(request: Request):
    # Aqui você pode verificar se o usuário está logado
    return render("dashboard.html", request)

# --- ROTA DE LOGOUT ---

@app.get("/logout")
async def fazer_logout():
    return RedirectResponse(url="/", status_code=303)