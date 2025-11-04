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

#print(access_payload)

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {access_payload}",
}

with httpx.Client(headers={"Accept": "application/json", "Authorization": f"Bearer {access_payload}",}) as client:
  data_response = client.get("http://localhost:8000/api/v1/users/me")

print(data_response.json())
print(data_response.status_code)