from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Class for getting the format we wish from the client
class User(BaseModel):
    name: str
    age: int
    password: str

# Class for sending the data format in the response body
class UserResponse(User):
    name:str
    age:int

@app.get("/user", response_model= UserResponse)
def get_user():
    return{
        "name": "Rubina",
        "age": "40",
        "password": 6767
    }
