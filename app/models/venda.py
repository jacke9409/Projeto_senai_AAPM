from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Venda(Base):
    __tablename__ = "vendas"
    id = Column(Integer, primary_key=True, index=True)
    associado_id = Column(Integer, ForeignKey("associados.id"))
    data = Column(DateTime, default=datetime.now)
    valor_total = Column(Float, nullable=False)
    metodo_pagamento = Column(String(30))
    status = Column(String(20), default="concluida")
    
    associado = relationship("Associado")
    itens = relationship("ItemVenda", back_populates="venda")

class ItemVenda(Base):
    __tablename__ = "itens_venda"
    id = Column(Integer, primary_key=True, index=True)
    venda_id = Column(Integer, ForeignKey("vendas.id"))
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)
    
    venda = relationship("Venda", back_populates="itens")
    produto = relationship("Produto")