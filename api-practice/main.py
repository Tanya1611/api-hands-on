from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "Welcome to Home Page."}

@app.get("/about")
def about():
    return {"about": ["This is about section."]}

@app.get("/users")
def users():
    return {"usernames":["Shamita","Geera","Chanchal"]}
