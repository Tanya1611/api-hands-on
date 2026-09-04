from fastapi import FastAPI

app = FastAPI()

# Dynamic Routes - Routes that change dynamically based on variables, such as a user ID (e.g., shifting automatically from /users/1 to /users/2).
@app.get("/users/{user_id}")
def get_users(user_id):
    return {
        "user_id" : user_id
    }


#Path Parameters: This refers to any dynamic value that changes directly inside the URL. 
# Instead of writing separate APIs for every single item, one API is written that handles multiple dynamic requests.
@app.get("/userPath/{user_id}")
def get_userPath(user_id:float):
    return {
        "user_id" : user_id
    }