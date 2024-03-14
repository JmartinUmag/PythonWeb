#para iniciar el servidor se usa uvicorn main:app --reload
import enum
from typing import Optional
from fastapi import FastAPI, Body, Query, Path
from pydantic import BaseModel, Field

class ItemName(str, enum.Enum):
    banana = "platano"
    orange = "naranja"
    apple = "manzana"

class Item[BaseModel]:
    name: str = Field(..., title="Name of the item", max_length=50)
    description: Optional[str] = None
    price: float = Field(..., gt=0, description="price of the item")
    tax: Optional[float] = None = Field(None, gt=0, description="tax of the item"

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "Hello, World!"}

@app.get("/users/me")
async def read_current_user():
    return {"user_id": "the current user"} 

@app.get("/users/{user_id}")
async def read_users(user_id: str):
    return {"user_id": user_id}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict["price_with_tax"]=price_with_tax
    return item_dict

@app.put("/items/{item_id}")
async def update_item(
    item: Item = Body(..., embed=True), #embed=True para que se pueda enviar el body como json y ... es para que sea requerido
    item_id: int = Path(..., gt=0), #gt es mayor que
    q: Optional[str] = Body(None, embed=True),
    ):
    results = {"item_id": item_id, **item.dict()}
    if q is not None:
        results["q"]= q
    return results


# @app.get("/items/{item}")
# async def read_item(item: ItemName, q:Optional[str] = None):
#     d= {"item": item}
#     if q is not None:
#         d["q"]=q
#     return d
 
#async def read_item(item: ItemName, skip: int=0, limit: int=30): se puede usar para paginacion
#    d= {"item": item}
#    return d

# @app.get("/users/{user_id}/items/{item_id}")
#primero se declara los parametros sin valor por defecto
# async def read_user_item(user_id: int, item_id: str, something: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": user_id, "something": something}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a long description"})
#     return item