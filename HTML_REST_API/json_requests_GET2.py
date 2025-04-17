import requests
import json


def send_get_request():
    url = "https://api.restful-api.dev/objects"

    params = {
        "id": ["ff808181932badb6019642bda11f102d"]
    }



    try:
        response = requests.get(url,params=params  )
        response.raise_for_status()  # Lève une erreur si problème HTTP

        result = response.json()
        for item in result:
            print(item)

    except requests.RequestException as e:
        print("error")

def Main():
    send_get_request()

if __name__ == "__main__":
    Main()