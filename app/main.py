from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Caminhos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # pasta app/
ROOT_DIR = os.path.dirname(BASE_DIR)  # pasta raiz do projeto

# ⚠️ CORREÇÃO: Static está dentro de app/static, não na raiz!
static_dir = os.path.join(BASE_DIR, "static")  # ← AGORA aponta para app/static
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Templates (pasta raiz)
templates_dir = os.path.join(ROOT_DIR, "templates")
templates = Jinja2Templates(directory=templates_dir)


def render(template_name: str, request: Request, extra_context: dict = None):
    context = {"request": request}
    if extra_context:
        context.update(extra_context)
    return templates.TemplateResponse(
        request=request,
        name=f"auth/{template_name}",
        context=context
    )


# =====================================================
# ROTAS
# =====================================================

@app.get("/", response_class=HTMLResponse)
def pagina_login(request: Request):
    return render("index.html", request)


@app.get("/visualizacao", response_class=HTMLResponse)
def pagina_visualizacao(request: Request):
    return render("visualizacao.html", request)


@app.get("/dashboard", response_class=HTMLResponse)
def pagina_dashboard(request: Request):
    return render("dashboard.html", request)


@app.post("/auth/login")
async def fazer_login(
    request: Request,
    username: str = Form(...),
    senha: str = Form(...)
):
    ADMIN_EMAIL = "admin@aapm.com"
    ADMIN_SENHA = "123456"
    
    if username == ADMIN_EMAIL and senha == ADMIN_SENHA:
        return RedirectResponse(url="/dashboard", status_code=303)
    else:
        return render("index.html", request, {"erro": "E-mail ou senha inválidos"})


@app.get("/logout")
async def fazer_logout():
    return RedirectResponse(url="/", status_code=303)


@app.get("/index")
async def redirect_index():
    return RedirectResponse(url="/", status_code=303)