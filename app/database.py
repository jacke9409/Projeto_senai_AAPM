from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Caminho para o banco de dados SQLite local (banco.db na raiz do projeto)
SQLALCHEMY_DATABASE_URL = "sqlite:///./banco.db"

# O 'check_same_thread=False' é necessário apenas para o SQLite trabalhar bem com o FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Configuração da fábrica de sessões do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe Base de onde todos os modelos (como o Usuario) vão herdar
Base = declarative_base()

# Função auxiliar (Dependency Injection) para usar nas rotas do FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Inicializa o banco de dados criando as tabelas se não existirem
def init_db():
    # Importa os modelos aqui dentro para evitar problemas de importação circular
    from app.models.usuario import Usuario
    from app.models.produto import Produto
    from app.models.categoria import Categoria
    from app.models.venda import Venda
    
    # Cria fisicamente as tabelas no seu banco.db
    Base.metadata.create_all(bind=engine)