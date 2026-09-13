from fastapi.testclient import TestClient
from pytest_file import app

client = TestClient(app)

'''
Testing ensures that APIs do not contain bugs or crash unexpectedly once deployed to a production environment
'''

#Test home api
def test_home():
    response = client.get("/home")

    # Check status code
    assert response.status_code == 200

    #Check Response data
    assert response.json() == {"message" : "Hello People"}


# Test add api
def test_add():
    response = client.get("/add?a=5&b=19")

    # Check status code
    assert response.status_code == 200

    #Check Response data
    assert response.json() == {"result": 24}


# Test multiplication api
def test_multiplication():
    response = client.get("/multiplication?a=10&b=2.5")

    # Check status code
    assert response.status_code == 200

    #Check Response data
    assert response.json() == {"result" : 25.0 }
