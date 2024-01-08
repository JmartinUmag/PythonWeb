from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:12345@localhost:3306/stock"
# root es usuario, 12345 es la contraseña, localhost es el servidor, 3306 es el puerto, stock es el nombre de la base de datos