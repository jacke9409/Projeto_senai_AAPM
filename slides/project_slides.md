# PDV AAPM — Apresentação do Código

---

## Objetivo

- Mostrar a arquitetura e os principais trechos do código do projeto PDV AAPM.
- Explicar como rodar, popular dados e testar login.

---

## Estrutura do projeto

- Root: [alembic.ini](../alembic.ini), [README.md](../README.md), [seed.py](../seed.py)
- App: [app/main.py](../app/main.py), [app/auth.py](../app/auth.py), [app/database.py](../app/database.py)
- Controllers: [app/controllers/usuario.controller.py](../app/controllers/usuario.controller.py), [app/controllers/produtos_controller.py](../app/controllers/produtos_controller.py)
- Models: [app/models/usuario.py](../app/models/usuario.py), [app/models/produto.py](../app/models/produto.py), [app/models/venda.py](../app/models/venda.py)
- Scripts: [scripts/create_user.py](../scripts/create_user.py), [scripts/seed_products.py](../scripts/seed_products.py)

---

## Fluxo de autenticação (visão geral)

1. Front-end: `auth/login.html` — formulário POST para `/api/login`
2. Backend: `app/auth.py` — rota `POST /api/login` valida email + senha
3. Em sucesso: redireciona para `/dashboard`

Trecho-chave (form):

```html
<form method="post" action="/api/login">
  <input type="email" name="email" />
  <input type="password" name="senha" />
  <button type="submit">Entrar</button>
</form>
```

---

## Modelo `Usuario` (resumo)

- Arquivo: [app/models/usuario.py](../app/models/usuario.py)
- Colunas relevantes: `id`, `nome`, `email`, `senha_hash`, `senha`, `role`, `criado_em`

Exemplo (simplificado):

```python
class Usuario(Base):
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100), unique=True)
    senha_hash = Column(String(255))
    senha = Column(String(255))  # atualmente usado para compatibilidade
```

---

## Models: `Produto` e `Venda` (resumo)

- `Produto`: [app/models/produto.py](../app/models/produto.py) — `nome`, `preco`, `quantidade_estoque`, `categoria`
- `Venda`: [app/models/venda.py](../app/models/venda.py) — `valor_total`, `metodo_pagamento`, relacionamento `itens`

---

## Scripts de preparação (seed)

- `scripts/seed_products.py` → executa `seed.py` e insere produtos de exemplo
- `scripts/create_user.py` → cria um usuário de teste (`admin@local` / `1234` por padrão)

Comandos:

```bash
python scripts/seed_products.py
python scripts/create_user.py
```

---

## Como rodar a aplicação localmente

1. (Opcional) criar ambiente virtual e instalar dependências.
2. Aplicar migrations (se usar Alembic):

```bash
python -m alembic revision --autogenerate -m "..."
python -m alembic upgrade head
```

3. Popular dados e criar usuário de teste (ver scripts acima).
4. Rodar servidor:

```bash
uvicorn app.main:app --reload
```

Abrir: `http://localhost:8000/login`

---

## Pontos de melhoria sugeridos

- Implementar hashing seguro de senhas (bcrypt) — não salvar senhas em texto.
- Implementar autenticação baseada em sessão ou JWT.
- Validar/normalizar campos do formulário no backend.
- Adicionar testes automatizados para login e endpoints críticos.

---

## Trecho: Rota de login (backend)

Arquivo: [app/auth.py](../app/auth.py)

```python
@router.post("/api/login")
async def login(request: Request, email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.email == email).first()
    if not user or (user.senha_hash != senha and user.senha != senha):
        return templates.TemplateResponse("auth/login.html", {"request": request, "error": "Credenciais inválidas"})
    return RedirectResponse(url="/dashboard", status_code=303)
```

---

## Fim / Contato

- Posso exportar isso para PowerPoint (`.pptx`) ou gerar um HTML com Reveal.js.
- Quer que eu gere o `.pptx` agora ou prefira Reveal.js/Markdown?
