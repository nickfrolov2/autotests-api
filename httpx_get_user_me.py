import httpx

login_payload = {
    "email": "nfrolov2@yandex.ru",
    "password": "Qwerty12345"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(login_response.json())
print(login_response.status_code)

access_payload = login_response_data["token"]["accessToken"]

print(access_payload)

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {access_payload}",
}

data_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(data_response.status_code)
print(data_response.json())
