# 1. Criar
python -m venv venv

# 2. Ativar
venv\Scripts\activate

# 3. Instalar
pip install fastapi uvicorn sqlalchemy jinja2

pip install python-multipart
pip install fastapi uvicorn sqlalchemy jinja2 python-multipart
# 4. Rodar o projeto
 python -m uvicorn app.main:app --reload

pip freeze > requirements.txt

pip install -r requirements.txt
# tirar bugs
python -m uvicorn app.main:app --reload --log-level debug