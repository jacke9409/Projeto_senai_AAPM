from app.database import SessionLocal
from app.models.produto import Produto

db = SessionLocal()

produtos_teste = [
    Produto(nome="Camisa Polo", preco=49.90, quantidade_estoque=30, categoria="Uniforme"),
    Produto(nome="Apostila Têxtil", preco=35.00, quantidade_estoque=50, categoria="Material"),
    Produto(nome="Kit Canetas", preco=15.50, quantidade_estoque=100, categoria="Papelaria"),
]

for p in produtos_teste:
    db.add(p)
db.commit()
print("Produtos inseridos com sucesso!")