from fastapi import FastAPI, status

app = FastAPI()

# Status Code
@app.post("/create_user", status_code= status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User is created."
    }

# Custom Responses
@app.get("/users", status_code= status.HTTP_200_OK)
def get_user():
    return {
        "success": "Successful",
        "message": "Getting the custom response",
        "data": {
            "name" : "Tortilla",
            "place" : "Mexico"
        }
    }