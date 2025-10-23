import requests

BASE_URL = "http://localhost:5000"

def test_hello():
    response = requests.get(f"{BASE_URL}/hello")
    assert response.status_code == 200, f"GET /hello failed: {response.text}"
    json_data = response.json()
    assert "message" in json_data and json_data["message"] == "Bienvenue !", "Unexpected response"
    print("✅ GET /hello passed.")


def test_echo():
    payload = {"nom": "Alice", "age": 30}
    headers = {"Content-Type": "application/json"}

    response = requests.post(f"{BASE_URL}/echo", json=payload, headers=headers)
    assert response.status_code == 200, f"POST /echo failed: {response.text}"
    json_data = response.json()
    assert json_data == payload, f"Unexpected response: {json_data}"
    print("✅ POST /echo passed.")


if __name__ == "__main__":
    test_hello()
    test_echo()
