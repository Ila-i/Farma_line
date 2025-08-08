from sqlalchemy import create_engine

DB_PATH = r"C:\Users\Utente\Desktop\FARMA_LINE2.db"
engine = create_engine(f"sqlite:///{DB_PATH}")
connection = engine.connect()