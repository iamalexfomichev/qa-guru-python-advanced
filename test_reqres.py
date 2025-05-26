import requests

def test_user_data():
    url = "https://reqres.in//api/users/2"
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.get(url, headers=headers)
    print(response.text)
    body = response.json()
    data = body["data"]

    expected_id = 2
    expected_email = "janet.weaver@reqres.in"

    assert data["id"] == expected_id
    assert data["email"] == expected_email

def test_invalid_user():
    url = "https://reqres.in/api/users/23"
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.get(url, headers=headers)


    assert response.status_code == 404
    assert response.json() == {}

def test_users_count_matches_per_page():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200

    data = response.json()
    assert len(data["data"]) == data["per_page"]

def test_create_user():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert "id" in body
    assert "createdAt" in body

def test_update_user():
    url = "https://reqres.in/api/users/2"
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.put(url, json=payload, headers=headers)

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert body["updatedAt"] is not None

def test_delete_user():
    url = "https://reqres.in/api/users/2"
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.delete(url, headers=headers)

    assert response.status_code == 204
    assert response.text == ""

def test_success_register():
    url = "https://reqres.in/api/register"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    body = response.json()
    assert "id" in body
    assert "token" in body