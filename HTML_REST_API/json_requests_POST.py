import requests
import json


def send_post_request():
    url = "https://api.restful-api.dev/objects"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "name": "Binome1-Carlos",
        "data": {
            "year": 2025,
            "price": 1849.99,
            "CPU model": "DELL",
            "Hard disk size": "1 TB"
        }
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Lève une erreur si problème HTTP

        result = response.json()
        print("result is --",result)

    except requests.RequestException as e:
        print("error")

def Main():
    send_post_request()

if __name__ == "__main__":
    Main()