import requests
import pytest

BASE_URL = "https://postman-echo.com"

def test_get_with_params():
    params = {"foo": "bar", "city": "New York"}
    response = requests.get(f"{BASE_URL}/get", params = params)
    assert response.status_code == 200, "А ожидали ответ 200"
    data = response.json()
    assert data["args"]["foo"] == "bar", "Параметр foo не совпадает"
    assert data["args"]["city"] == "New York", "Параметр city не совпадает"

def test_post_name_and_role():
    payload = {"name": "Evgenia", "role": "QA"}
    response = requests.post(f"{BASE_URL}/post", json = payload)
    assert response.status_code == 200, "Ожидали ответ 200"
    data = response.json()
    assert data["json"]["name"] == "Evgenia", "Параметр name не совпадает"
    assert data["json"]["role"] == "QA", "Параметр role не совпадает"

def test_get_headers():
    headers = {"Accept-Language" : "RU"}
    response = requests.get(f"{BASE_URL}/get", headers = headers)
    assert response.status_code == 200, "Ожидали ответ 200"
    data = response.json()
    assert data["headers"]["accept-language"] == "RU"

def test_delete_params():
    params = {"ID" : "1234", "name" : "Elena"}
    response = requests.delete(f"{BASE_URL}/delete", params = params)
    assert response.status_code == 200, "Ожидали ответ 200"

def test_put_():
    payload = {"id": 1, "title": "Updated Task", "status": "done"}
    response = requests.put(f"{BASE_URL}/put", json = payload)
    assert response.status_code == 200, "Ожидали ответ 200"



