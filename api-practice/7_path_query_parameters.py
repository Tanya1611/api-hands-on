from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

'''
Example:
PUT /users/101?notify=true
{
    "name": "Mallory",
    "age": 32
}

Path parameter(ie. 101) & Query parameter(ie, notify=true)
'''

users = []

# Class for user details & wrapping BaseModel in it
class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return{
        "message": "User Created",
        "data": user
    }

@app.put("/users/{user_id}")
def updated_function(user_id: int, user: User, notify: bool = False):
    if user_id < len(users):
        users[user_id] = user

        return{
            "message": "User Updated!",
            "notify": notify,
            "data": user
        }
    return{
        "Error": "User not found."
    }

@app.get("/users")
def get_users():
    return{
        "data": users
    }