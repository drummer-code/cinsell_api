from pydantic import BaseModel


class UserIn(BaseModel):
    username: str
    password: str
 

class UserOut(BaseModel):
    username: str
    nDocumento:int
    nombre:str
    telefono:int
    ciudad:str
    departamento:str
    direccion:str 

class User(BaseModel):
    username: str