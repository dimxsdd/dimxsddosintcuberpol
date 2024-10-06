def format_results(results):
    if not results:
        return "Нет данных"
    
    formatted_results = []
    
    for title, data in results.items():
        formatted_results.append(f"{title}:")
        
        # Убираем вывод Number of Results
        # formatted_results.append(f"  Number of Results: {data['NumOfResults']}")  # Убираем эту строку
        
        for entry in data['Data']:
            formatted_results.append(f"    Повне ім'я: {entry.get('FullName', 'Немає даних')}")
            formatted_results.append(f"    Адреса: {entry.get('Address', 'Немає даних')}")
            formatted_results.append(f"    Місце народження: {entry.get('PlaceBirth', 'Немає даних')}")
            formatted_results.append(f"    Дільниця: {entry.get('PollingStation', 'Немає даних')}")
            formatted_results.append(f"    Дата народження: {entry.get('BDay', 'Немає даних')}")
            formatted_results.append("")  # Пустая строка для разделения записей
    
    return "\n".join(formatted_results)
