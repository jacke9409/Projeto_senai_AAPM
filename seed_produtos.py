from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.produto import Produto
from app.models.categoria import Categoria

produtos_info = [
    ("Camisa Polo", 49.90, 30, "Uniforme"),
    ("Apostila Têxtil", 35.00, 50, "Material"),
    ("Kit Canetas", 15.50, 100, "Papelaria"),
    ("Abridor de casa", 0.00, 0, "Costura / Confecção"),
    ("Agulha de máquina", 0.00, 0, "Costura / Confecção"),
    ("Alfinete cabeça colorida", 0.00, 0, "Costura / Confecção"),
    ("Alicate pique", 0.00, 0, "Costura / Confecção"),
    ("Almofada", 0.00, 0, "Costura / Confecção"),
    ("Apontador", 0.00, 0, "Papelaria"),
    ("Avental", 0.00, 0, "Costura / Confecção"),
    ("Bobina", 0.00, 0, "Costura / Confecção"),
    ("Bola de pebolim", 0.00, 0, "Lazer / Esportes"),
    ("Bola de ping pong", 0.00, 0, "Lazer / Esportes"),
    ("Bolsa senai", 0.00, 0, "Outros"),
    ("Borracha branca", 0.00, 0, "Papelaria"),
    ("Borracha caneta", 0.00, 0, "Papelaria"),
    ("Cabo usb tipo c", 0.00, 0, "Eletrônicos"),
    ("Caixa de bobina", 0.00, 0, "Costura / Confecção"),
    ("Calculadora", 0.00, 0, "Papelaria"),
    ("Camisa malha branca", 0.00, 0, "Costura / Confecção"),
    ("Camisa malha preta", 0.00, 0, "Costura / Confecção"),
    ("Camiseta polo de malha preta", 0.00, 0, "Costura / Confecção"),
    ("Caneta bic", 0.00, 0, "Papelaria"),
    ("Caneta mágica fantasminha colorida", 0.00, 0, "Papelaria"),
    ("Caneta marca texto", 0.00, 0, "Papelaria"),
    ("Caneta para desenho faber castell 0.4", 0.00, 0, "Papelaria"),
    ("Canetinha colorida 12 cores", 0.00, 0, "Papelaria"),
    ("Carregador de celular v8 usb", 0.00, 0, "Eletrônicos"),
    ("Carretilha cabo de madeira", 0.00, 0, "Costura / Confecção"),
    ("Cola bastão", 0.00, 0, "Papelaria"),
    ("Cola líquida", 0.00, 0, "Papelaria"),
    ("Compasso", 0.00, 0, "Papelaria"),
    ("Cordão para crachá senai", 0.00, 0, "Outros"),
    ("Corretivo (fita corretiva)", 0.00, 0, "Papelaria"),
    ("Curva francesa grande 1119", 0.00, 0, "Costura / Confecção"),
    ("Durex", 0.00, 0, "Papelaria"),
    ("Esfuminho", 0.00, 0, "Papelaria"),
    ("Esquadro", 0.00, 0, "Papelaria"),
]


def criar_categorias_e_produtos():
    db: Session = SessionLocal()
    try:
        # Criar categorias únicas
        nomes_categorias = set([c for (_, _, _, c) in produtos_info])
        categoria_map = {}
        for nome in nomes_categorias:
            cat = db.query(Categoria).filter(Categoria.nome == nome).first()
            if not cat:
                cat = Categoria(nome=nome)
                db.add(cat)
                db.commit()
                db.refresh(cat)
            categoria_map[nome] = cat.id

        # Inserir produtos usados os categoria_id
        for nome, preco, qtd, categoria in produtos_info:
            prod = Produto(
                nome=nome,
                preco=preco,
                quantidade_estoque=qtd,
                categoria_id=categoria_map[categoria]
            )
            db.add(prod)
        db.commit()
        print("Produtos e categorias inseridos com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir produtos: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    criar_categorias_e_produtos()
