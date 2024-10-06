import requests

def fetch_osint_data(query):
    key = "6310113267:KAqmfsF7"
    url = 'https://server.leakosint.com/'

    data = {
        "token": key,
        "request": query,
        "limit": 100,
        "lang": "ru"
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        result = response.json()
        
        # Извлечение данных из ответа
        if 'List' in result:
            return result['List']  # Возвращаем только список
        else:
            print("Нет списка в ответе API")
            return []
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except ValueError as json_err:
        print(f"JSON decoding error: {json_err}")
        print(f"Response text: {response.text}")  # Выводим текст ответа для отладки
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
