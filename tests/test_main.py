from fastapi.testclient import TestClient

#Import the FastAPI app instance from the controller module
from main import app

#Create a TestClient instance for the FastAPI app
client = TestClient(app)

#Define a test function for reading a specific sheep
def test_read_sheep():
    #Send a GET request to the endpoint "/sheep/1"
    response = client.get("/sheep/1")

    # Assert that the response status code is 200 (0K)
    assert response.status_code == 200

    #Assert that the response JSON matches the expected data
    assert response.json() == {
        #Expected JSON structure
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }


#Define a test function for adding a new sheep
def test_add_sheep():

    #New sheep data
    new_sheep = {
        "id": 7,
        "name": "Sutton",
        "breed": "Suffolk",
        "sex": "ewe"
    }

    #sending a POST request for the new sheep creation
    response = client.post("/sheep/", json=new_sheep)

    #Assert that response code is 201(created)
    assert response.status_code == 201

    #Assert that response JSON matches new sheep data
    assert response.json() == new_sheep

    #Assert that new sheep data was added to the database
    #retrieving sheep by ID
    assert client.get("/sheep/7").json() == new_sheep



def test_update_sheep():

    #Altered sheep data
    new_sheep = {
        "id": 1,
        "name": "This has been altered",
        "breed": "This has been altered",
        "sex": "This has been altered"
    }

    #Sending a PUT request for the altered sheep data
    response = client.put("/sheep/1", json=new_sheep)

    #Asserting that the response code given is 200(OK)
    assert response.status_code == 200

    #Assert that response JSON matches altered sheep data
    assert response.json() == new_sheep

    #Assert that existing sheep's data was altered
    assert client.get("/sheep/1").json() == new_sheep


def test_delete_sheep():
    #Send a DELETE request
    response = client.delete("/sheep/1")

    #Assert that server response code is 204(NO_CONTENT)
    assert response.status_code == 204

    #Assert that sheep is deleted from data
    assert client.get("/sheep/1").status_code == 404


def test_read_all_sheep():

    #Send a GET request for all sheep
    response = client.get("/sheep")

    #Assert that response code is 200(OK)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 6
    sample_sheep = data[5]
    assert "id" in sample_sheep
    assert "name" in sample_sheep
    assert "breed" in sample_sheep
    assert "sex" in sample_sheep
