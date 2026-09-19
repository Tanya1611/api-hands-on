from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

# def task():
#     time.sleep(3)
#     return "Done"

# async def task():
#     await asyncio.sleep(3)
#     return "Done"

'''
Dependency Injection -> A design pattern where a function or logic required by another function is automatically executed and injected.

Basic Execution Flow: When a request is received, the dependency is executed first; 
> if it succeeds -> the main API route runs, but if it fails -> an exception is returned.

'''
@app.get("/home")
async def home():
    await asyncio.sleep(3)
    return{
        "message":"Async API"
    }