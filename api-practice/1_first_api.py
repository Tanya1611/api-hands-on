'''
API (Application Programming Interface): Acts as a bridge between the front-end and the back-end. 
> The front-end sends a request, and the API fetches the requested data from the database and returns it.

FastAPI: It is a modern Python web framework designed specifically for building fast, high-performance APIs.
> Benefit -> Exceptional Speed, Asynchronous Support, Automatic API Documentation, Automatic Data Validation, Easy to Learn.

Route: A URL path (for example, / for the home page, /about for the about page, or /users for a user page). 
> Every route in FastAPI is attached to a specific Python function that automatically executes when that path is accessed.

GET Request: Used strictly to fetch or read data from a server. 
> Common real-world examples include searching on Google, loading Instagram feeds, or browsing products on Amazon. 
> It does not change or modify any database data; it only reads it.
'''

from fastapi import FastAPI

#Create an application object instance 
app = FastAPI()

#Home Route
@app.get("/")
def read_root():
    return {"message" : "Welcome to Home Page."}

@app.get("/about")
def about():
    return {"about": ["This is about section."]}

@app.get("/users")
def users():
    return {"usernames":["Geiku","Medusa","Zouya"]}
 