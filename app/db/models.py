from app.db.models import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class User(Base):
    
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)
    telefono = Column(Integer)
    estado = Column(Boolean) #Estado del usuario activo o inactivo

class UserId