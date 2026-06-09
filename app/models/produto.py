from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Produto(Base):
    __tablename__ = "produtos"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(200), nullable=True)
    preco = Column(Float, nullable=False)
    quantidade_estoque = Column(Integer, default=0)
    ativo = Column(Boolean, default=True)
    
    # Chave Estrangeira (vincula o produto ao ID da tabela categorias)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    
    # Relacionamento virtual do SQLAlchemy para acessar a categoria direto pelo objeto
    categoria = relationship("Categoria", back_populates="produtos")