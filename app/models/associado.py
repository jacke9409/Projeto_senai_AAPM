from sqlalchemy import Column, Integer, String, Date, Boolean
from app.database import Base

class Associado(Base):
    __tablename__ = "associados"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    ra = Column(String(20), unique=True, nullable=False)
    curso = Column(String(50))
    email = Column(String(100), unique=True)
    telefone = Column(String(20))
    data_associacao = Column(Date)
    status = Column(Boolean, default=True)