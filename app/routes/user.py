from fastapi import APIRouter, Depends
from app.schemas import User, UserId
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models

#se hace referencia desde main a esta parte
router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get('/')
def index():
    return {"message": "Hola"}

@router.get('/obtener_usuarios')
def obtener_usuarios(db: Session = Depends(get_db)):
    us= db.query(models.User).all()
    print(us)
    return us

@router.post('/crear_usuarios')
def crear_usuarios(db: Session = Depends(get_db)):
    usuario = User.model_dump()
    nuevo_usuario = models.User(
        username= usuario["username"],
        password= usuario["password"],
        name= usuario["name"],
        surname= usuario["surname"],
        email= usuario["email"]
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    print (usuario)
    return ("Usuario creado exitosamente")
'''
@router.post('/{user_id}') #para probar se puede usar get
def obtener_usuario(user_id: int):
    for user in usuarios:
        print(user, type(user))
        if user["id"] == user_id:
            return {"usuario": user}
    return "Usuario no encontrado"

@router.post('/obtener_usuario2') #para obtener paramertro por JSON se usa un modelo y luego esto
def obtener_usuario_2(user_id:UserId):
    for user in usuarios:
        if user["id"] == user_id.id:
            return {"usuario": user}
    return "Usuario no encontrado"

@router.delete('/{user_id}')
def eliminar_usuario(user_id: int):
    for i, user in enumerate(usuarios):
        if user["id"] == user_id:
            usuarios.pop(i)
            return "Usuario eliminado"
    return "Usuario no encontrado"

@router.put('/{user_id}')
def actualizar_usuario(user_id: int, updateUser: User):
    for i in range(len(usuarios)):
        if usuarios[i]["id"] == user_id:
            usuarios[i]["id"] = updateUser.dict()["id"]
            usuarios[i]["nombre"] = updateUser.dict()["nombre"]
            usuarios[i]["apellido"] = updateUser.dict()["apellido"]
            usuarios[i]["telefono"] = updateUser.dict()["telefono"]
            return "Usuario actualizado"
    return "Usuario no encontrado"
'''