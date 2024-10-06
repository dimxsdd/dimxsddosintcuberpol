import requests

def fetch_car_data(number):
    key = "105b1c14538446a81832384f2e7e82fe"  # API ключ для ГАИ
    url = f"https://baza-gai.com.ua/nomer/{number}"

    try:
        response = requests.get(url, headers={"Accept": "application/json", "X-Api-Key": key})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
