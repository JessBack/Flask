class Config:
    USER = "root"              # Nome de usuário do MySQL
    PASSWORD = ""              # Senha do MySQL (se houver)
    HOST = "localhost"         # Host do banco de dados (pode ser 'localhost')
    DATABASE = "ecommerce"     # Nome do banco de dados
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    SECRET_KEY = "minha_chave_123"  # Corrigido o nome para SECRET_KEY
