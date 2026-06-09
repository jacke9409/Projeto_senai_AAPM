from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.usuario import Usuario
# Importa a função de hash que está no arquivo auth.py de vocês
from auth import hash_senha 

def criar_admin_padrao():
    db: Session = SessionLocal()
    
    try:
        # Verifica se o admin já existe pelo e-mail
        admin_existente = db.query(Usuario).filter(Usuario.email == "admin@senai.com").first()
        
        if not admin_existente:
            print("Criando usuário administrador padrão com senha criptografada...")
            
            # Aqui usamos a função do auth.py para gerar o hash seguro
            senha_segura = hash_senha("senai123")
            
            admin = Usuario(
                nome="Gidalva Administradora",
                email="admin@senai.com",
                senha_hash=senha_segura,  # Salva o hash gerado pelo bcrypt
                role="admin",
                ativo=True
            )
            
            db.add(admin)
            db.commit()
            print("✨ Usuário administrador criado com sucesso no banco!")
            print("📧 Email: admin@senai.com | 🔑 Senha original: senai123")
        else:
            print("ℹ️ O usuário administrador já existe no banco de dados.")
            
    except Exception as e:
        print(f"❌ Erro ao rodar o seed: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    criar_admin_padrao()