from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel #modelo con el cual se reciben los datos

class User(BaseModel): #Esquema
    id: int
    nombre: str
    apellido: str
    telefono: int

class UserId(BaseModel):
    id: int

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

@app.post('/usuario/{user_id}') #para probar se puede usar get
def obtener_usuario(user_id: int):
    for user in usuarios:
        print(user, type(user))
        if user["id"] == user_id:
            return {"usuario": user}
    return "Usuario no encontrado"

@app.post('/obtener_usuario2') #para obtener paramertro por JSON se usa un modelo y luego esto
def obtener_usuario_2(user_id:UserId):
    for user in usuarios:
        if user["id"] == user_id.id:
            return {"usuario": user}
    return "Usuario no encontrado"

@app.delete('/usuario/{user_id}')
def eliminar_usuario(user_id: int):
    for user in usuarios:
        if user["id"] == user_id:
            usuarios.pop(user)
            return "Usuario eliminado"
    return "Usuario no encontrado"

@app.put('/usuario/{user_id}')
def actualizar_usuario(user_id: int, updateUser: User):
    for i in range(len(usuarios)):
        if usuarios[i]["id"] == user_id:
            usuarios[i]["id"] = updateUser.dict()["id"]
            usuarios[i]["nombre"] = updateUser.dict()["nombre"]
            usuarios[i]["apellido"] = updateUser.dict()["apellido"]
            usuarios[i]["telefono"] = updateUser.dict()["telefono"]
            return "Usuario actualizado"
    return "Usuario no encontrado"

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
