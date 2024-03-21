from pydantic import BaseModel #modelo con el cual se reciben los datos
from typing import Optional
from datetime import datetime


class User(BaseModel): #Esquema
    id: int
    nombre: str
    apellido: str
    telefono: int

class UserId(BaseModel):
    id: int


class Data(BaseModel):
    id: int
    date: datetime
    time: str
    site: str

class Col(BaseModel):
    id: int
    min: float
    median: float
    max: float
    index: int

class Stat(BaseModel):
    id: int
    min_abs: float
    median_abs: float
    max_abs: float
    mean: Optional[float] = None
    mode: Optional[float] = None

class File(BaseModel):
    id: int
    name_cols: str

class Image(BaseModel):
    id: int
    name: str


