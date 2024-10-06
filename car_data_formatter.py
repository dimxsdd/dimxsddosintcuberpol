def format_car_data(data):
    if not data or not data.get("model"):
        return "Нет данных"
    
    formatted_data = f"<h3>Информация о автомобиле:</h3>"
    formatted_data += f"<p><strong>Модель:</strong> {data['model']} ({data['model_year']})</p>"
    formatted_data += f"<p><strong>VIN:</strong> {data['vin']}</p>"
    formatted_data += f"<p><strong>Номер:</strong> {data['digits']}</p>"
    formatted_data += f"<p><strong>Цвет:</strong> {data['operations'][0]['color']['ua']}</p>"
    formatted_data += f"<p><strong>Состояние:</strong> {'Угон' if data.get('is_stolen') else 'Не угнан'}</p>"
    formatted_data += f"<img src='{data['photo_url']}' alt='Фото автомобиля' style='width:100%; max-width:300px;'/>"
    return formatted_data
