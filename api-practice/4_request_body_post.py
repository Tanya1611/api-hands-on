from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

'''
Post Request when accepting request body through Parameters passed in function
'''
@app.post("/product1")
def create_product(name: str, quantity: int):
    return {
        "name" : name,
        "quantity" : quantity
    }



'''
Post Request when accepting request body data as a dictionary.
-> Accepting raw dictionaries provides no data validation.
-> Highly flexible and returns whatever data the client sends.  
-> Any input—valid or invalid—is accepted and returned without checking. 
-> Have to write manual validation code to prevent errors if needed.
'''
@app.post("/product2")
def create_product2(user: dict):
    return{
        "message" : "Product Created!",
        "data" : user
    }


'''
Post request with Pydantic for strict validations
-> Shows json request schema in body
-> Allows developers to define strict data structures and perform automatic validation.
'''
class User(BaseModel):
    product_name : str
    product_qty : float

@app.post("/product3")
def create_product3(user : User):
    return{
        "message" : "Product created!!",
        "data" : user
    }
