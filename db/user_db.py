from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    
database_users = Dict[str, UserInDB]
database_users = {
"jessid22": UserInDB(**{"username":"jessid22",
                        "password":"lider"}),
"emmanuel35": UserInDB(**{"username":"emmanuel35",
                        "password":"sensey"}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None
def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db
