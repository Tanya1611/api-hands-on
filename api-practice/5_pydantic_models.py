from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# A Pydantic Model is a schema structure that defines the exact format of the incoming data.
class UserSchema(BaseModel):
    name: str
    age: int
    email: str

@app.post("/createUser")
def create_user(user: UserSchema):
    return {
        "message": "User is created!!",
        "data": user
    }

# Handling Nested data models
class Address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    age: int
    address: Address

@app.post("/creatNestedUser")
def create_nested_user(user: User):
    return{
        "User": user
    }