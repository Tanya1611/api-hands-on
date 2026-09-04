from fastapi import FastAPI

app = FastAPI()

'''
Query Parameters refer to extra data sent at the end of a URL, represented as key-value pairs following a question mark (?)

> When a parameter in a route's function is defined, FastAPI expects that parameter by default. - Becomes required
'''
@app.get("/users")
def get_users(name):  
    return {"Name":name}


''' 
Optional Query Parameters
> To prevent errors when a query parameter is missing, field can be made optional by setting its default value to None.
'''
@app.get("/users2")
def get_users(name: str = None):  
    return {"Name":name}


''' 
Default Query Parameters
> A specific default value to a parameter in the function signature can be assigned.
> If the user provides a value, FastAPI overrides the default and uses the user's provided value.
'''
@app.get("/users3")
def get_users3(limit: int = 15):
    return {"Limit" : limit}


'''
Multiple query parameters
> Multiple query parameters in a single route can be accepted by defining multiple arguments in your function.
'''
@app.get("/users4")
def get_users4(name: str = None, limit: int = 15):
    return {
        "Name":name,
        "Limit" : limit
        }