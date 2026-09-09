from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

'''
Exception Handling: A mechanism to manage and respond to errors gracefully when something goes wrong in the code.

HTTPException: FastAPI’s built-in exception class that allows us to easily raise HTTP errors (like returning a 404 Not Found or 400 Bad Request) directly from the route handlers.
'''

#Basic HTTPException
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id != 101:
        raise HTTPException(
            status_code= 404,
            detail= "User Not Found!"
        )
    return {
        "id" : 101,
        "name" : "Marchello"
    }


# Custom Exception (User Defined Exception)

class UserNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.get("/customUsers/{name}")
def get_user_name(name: str):
    if name != "Maria":
        raise UserNotFoundException(name)
    return {
        "name": name
    }

'''
Point: Simply raising a custom Python exception without a handler causes FastAPI to return a generic 500 Internal Server Error, which is unhelpful to the client.

Global Exception Handler is a centralized function registered using @app.exception_handler(CustomException).
> It intercepts specific custom exceptions globally, allowing us to return a consistent, formatted JSONResponse
'''
# Global Exception Handler
@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": f"User {exc.name} not found!"
        }
    )