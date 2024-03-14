from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel #modelo con el cual se reciben los datos

class User(BaseModel): #Esquema
    id: int
    nombre: str
    apellido: str
    edad: int

app = FastAPI()
usuarios = []

@app.get('/')
def index():
    return {"message": "Hola"}

@app.get('/usuario')
def obtener_usuarios():
    return usuarios

@app.post('/usuario')
def crear_usuario(user:User): #variable user recibe el modelo usado
    #print(user)
    #print(user.id)
    usuario = user.dict()
    usuarios.append(usuario)
    print (usuario)
    return "Usuario creado exitosamente"

@app.get('/usuario/{user_id}')
def obtener_usuario(user_id: int):
    for user in usuarios:
        print(user, type(user))
        if user["id"] == user_id:
            return {"usuario": user}
    return "Usuario no encontrado"

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
