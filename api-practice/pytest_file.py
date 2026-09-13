from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def home():
    return {
        "message" : "Hello People"
    }

@app.get("/add")
def add(a: int, b:int):
    return{
        "result": a+b
    }

@app.get("/multiplication")
def multiplication(a: int, b:float):
    return{
        "result": a*b
    }