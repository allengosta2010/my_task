import requests


def test_add_new_pet_a_store_success():
    body = {
        "id": 10,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.post("https://petstore.swagger.io/v2/pet", json=body)
    deserialized_response = response.json()
    assert response.status_code == 200
    assert deserialized_response['id'] == body['id']


def test_add_new_pet_a_store_fail():
    error_body = {
        "id": "0"
    }
    response = requests.post("https://petstore.swagger.io/v2/pet", json=error_body)
    print(response.text)
    assert response.status_code == 400
    # assert deserialized_response['id'] == error_body['id']


def test_change_new_pet_a_store_success():
    body = {
        "id": 10,
        "category": {
            "id": "0",
            "name": "string11"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.put("https://petstore.swagger.io/v2/pet", json=body)
    deserialized_response = response.json()
    assert response.status_code == 200
    assert deserialized_response['id'] == body['id']


def test_change_new_pet_a_store_fail():
    error_body = {
        "id": "0"
    }
    response = requests.put("https://petstore.swagger.io/v2/pet", json=error_body)
    print(response.text)
    assert response.status_code == 400
    # assert deserialized_response['id'] == error_body['id']


def test_find_by_status_success():
    response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
    assert response.status_code == 200


def test_find_by_status_fail():
    response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=testify")
    print(response.text)
    assert response.status_code == 400

