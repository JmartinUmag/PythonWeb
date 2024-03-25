from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/DB_Prototype"
engine=create_engine(SQLALCHEMY_DATABASE_URL) #el engine es el que se encarga de la conexion a la base de datos

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #se crea una sesion local para la base de datos
Base = declarative_base() #se crea una base para empezar a crear los modelos, es el que se hereda

#esto devuelve la sesion de la base de datos

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() #cierra la conexion a la base de datos