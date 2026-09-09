#Resuse and clean structure

from fastapi import FastAPI, Depends

app =   FastAPI()

'''
Dependency Injection is a design pattern where a function's dependencies (helper logic or external resources) are automatically provided from an external source rather than being hardcoded inside the function itself.

'''

def common_logic():
    return{
        "message": "Common logic executed."
    }

@app.get("/home")
def home(data= Depends(common_logic)):
    return data

@app.get("/tent")
def tent(data= Depends(common_logic)):
    return data