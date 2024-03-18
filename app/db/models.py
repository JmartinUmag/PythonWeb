
"""

class User(BaseModel): #Esquema
    id: int
    nombre: str
    apellido: str
    telefono: int

    """

from app.db.models import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)
    telefono = Column(Integer)

class UserId