from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fastapi-database"
engine=create_engine(SQLALCHEMY_DATABASE_URL) #el engine es el que se encarga de la conexion a la base de datos

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #se crea una sesion local para la base de datos
Base = declarative_base() #se crea una base para empezar a crear los modelos, es el que se hereda