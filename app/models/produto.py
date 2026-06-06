from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(200))
    preco = Column(Float, nullable=False)
    quantidade_estoque = Column(Integer, default=0)
    categoria = Column(String(50))
    ativo = Column(Boolean, default=True)