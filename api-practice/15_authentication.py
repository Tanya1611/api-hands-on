from fastapi import FastAPI, HTTPException, Depends, Header
from jose import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

# Make a secure key
SECRET_KEY = "my_secret_key"

# Using a symmetric encryption algorithm
ALGORITHM = "HS256"  

# Function of creating a token
def create_token(data: dict):
    to_encode = data.copy()
    expiry = datetime.now(timezone.utc) + timedelta(minutes=2)

    #Add expiry to api payload
    to_encode.update({
        "exp": expiry
    })

    # Create jwt token
    token = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    return token

# Generate the token via Login API
@app.post("/login")
def login(username: str, password: str):
    # Dummy authentication
    if username != "admin" or password != "1234":
        raise HTTPException(
            status_code=401,
            detail="Invalid username and password"
        )
    token = create_token({
        "sub": username
    })
    return {
        "access_token": token
    }

# Token Verification
def verify_token(token: str = Header(None)):
    try:
        # Check token existence
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired Token"
        )

# Acess token only after verification
# Protected Route
@app.get("/secure")
def secure_data(user = Depends(verify_token)):
    return{
        "message": "Secured Data Accessed",
        "user": user
    }