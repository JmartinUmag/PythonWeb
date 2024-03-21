from fastapi import FastAPI
import uvicorn
from app.db.database import Base, engine
from app.routes import user

def create_tables():
    Base.metadata.create_all(bind=engine) #para crear las tablas en la base de datos

create_tables()

app = FastAPI()
app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
