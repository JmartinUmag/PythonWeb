from pydantic import BaseModel #modelo con el cual se reciben los datos

class User(BaseModel): #Esquema
    id: int
    nombre: str
    apellido: str
    telefono: int

class UserId(BaseModel):
    id: int