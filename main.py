from fastapi import FastAPI
from fastapi import HTTPException
from db.user_db import UserInDB
from db.user_db import get_user,update_user
from models.user_models import UserIn,UserOut,User

app =FastAPI()

@app.post("/login/")
async def users_post(user_in:UserIn):
    user = get_user(user_in.username)
    if user == None:
        raise HTTPException(status_code=404,
    detail="El usuario no existe")
    if user.password != user_in.password:
            return {"Autenticado": False}
    return {"Autenticado": True}

@app.get("/users/")
async def users_get(user_in:User):
    user = get_user(user_in.username)
    if user == None:
        raise HTTPException(status_code=404,
    detail="El usuario no existe")
    user_out = UserOut(**user.dict())
    return user_out
