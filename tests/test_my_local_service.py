import os

import requests

def test_health_check(app_url):  # Проверка работоспособности сервиса
    response = requests.get(f"{app_url}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_user_data(app_url): #Проверка данных пользователя

    response = requests.get(f"{app_url}/api/users?page=2")
    print(response.text)
    assert response.status_code == 200
    user_data = response.json()["data"][0]
    expected_id = 7
    expected_email = "michael.lawson@reqres.in"
    assert user_data["id"] == expected_id
    assert user_data["email"] == expected_email


def test_invalid_user(app_url):     # Проверка на несуществующего пользователя

    #url = "http://localhost:8000/api/users/23"
    response = requests.get(f"{app_url}/api/users/23")
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_users_count_matches_per_page(app_url):   # Проверка, что количество пользователей соответствует количеству на странице
    response = requests.get(f"{app_url}/api/users?page=2")
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) == data["per_page"]


def test_create_user(app_url):   # Проверка создания пользователя
    #url = "http://localhost:8000/api/users"
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(f"{app_url}/api/users", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert "id" in body
    assert "createdAt" in body


def test_update_user(app_url): # Проверка обновления пользователя
    url = f"{app_url}/api/users/2"
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert body["updatedAt"] is not None


def test_delete_user(app_url): # Проверка удаления пользователя
    url = f"{app_url}/api/users/2"
    response = requests.delete(url)
    assert response.status_code == 204
    assert response.text == ""


def test_success_register(app_url): # Проверка успешной регистрации пользователя
    url = f"{app_url}/api/register"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "id" in body
    assert "token" in body
