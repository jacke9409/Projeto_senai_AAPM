from app.database import SessionLocal
from app.models.produto import Produto

db = SessionLocal()

produtos_teste = [
    Produto(nome="Camisa Polo", preco=49.90, quantidade_estoque=30, categoria="Uniforme"),
    Produto(nome="Apostila Têxtil", preco=35.00, quantidade_estoque=50, categoria="Material"),
    Produto(nome="Kit Canetas", preco=15.50, quantidade_estoque=100, categoria="Papelaria"),
    Produto(nome="Abridor de casa", preco=0.00, quantidade_estoque=0, categoria="Costura / Confecção"),
    Produto(nome="Agulha de máquina", preco=0.00, quantidade_estoque=0, categoria="Costura / Confecção"),
    Produto(nome="Alfinete cabeça colorida", preco=0.00, quantidade_estoque=0, categoria="Costura / Confecção"),
    Produto(nome="Alicate pique", preco=0.00, quantidade_estoque=0, categoria="Costura / Confecção"),
    Produto(nome="Almofada", preco=0.00, quantidade_estoque=0, categoria="Costura / Confecção"),
    Produto(nome="Apontador", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Avental", preco=0.00, quantidade_estoque=0, categoria="Costura / Confecção"),
    Produto(nome="Bobina", preco=0.00, quantidade_estoque=0, categoria="Costura / Confecção"),
    Produto(nome="Bola de pebolim", preco=0.00, quantidade_estoque=0, categoria="Lazer / Esportes"),
    Produto(nome="Bola de ping pong", preco=0.00, quantidade_estoque=0, categoria="Lazer / Esportes"),
    Produto(nome="Bolsa senai", preco=0.00, quantidade_estoque=0, categoria="Outros"),
    Produto(nome="Borracha branca", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Borracha caneta", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Cabo usb tipo c", preco=0.00, quantidade_estoque=0, categoria="Eletrônicos"),
    Produto(nome="Caixa de bobina", preco=0.00, quantidade_estoque=0, categoria="Costura / Confecção"),
    Produto(nome="Calculadora", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Camisa malha branca", preco=0.00, quantidade_estoque=0, categoria="Costura / Confecção"),
    Produto(nome="Camisa malha preta", preco=0.00, quantidade_estoque=0, categoria="Costura / Confecção"),
    Produto(nome="Camiseta polo de malha preta", preco=0.00, quantidade_estoque=0, categoria="Costura / Confecção"),
    Produto(nome="Caneta bic", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Caneta mágica fantasminha colorida", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Caneta marca texto", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Caneta para desenho faber castell 0.4", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Canetinha colorida 12 cores", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Carregador de celular v8 usb", preco=0.00, quantidade_estoque=0, categoria="Eletrônicos"),
    Produto(nome="Carretilha cabo de madeira", preco=0.00, quantidade_estoque=0, categoria="Costura / Confecção"),
    Produto(nome="Cola bastão", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Cola líquida", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Compasso", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Cordão para crachá senai", preco=0.00, quantidade_estoque=0, categoria="Outros"),
    Produto(nome="Corretivo (fita corretiva)", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Curva francesa grande 1119", preco=0.00, quantidade_estoque=0, categoria="Costura / Confecção"),
    Produto(nome="Durex", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Esfuminho", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
    Produto(nome="Esquadro", preco=0.00, quantidade_estoque=0, categoria="Papelaria"),
]


for p in produtos_teste:
    db.add(p)
db.commit()
print("Produtos inseridos com sucesso!")