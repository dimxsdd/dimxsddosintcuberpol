from flask import Flask, render_template, request, jsonify
from api_fetcher import fetch_osint_data
from car_api_request import fetch_car_data
from car_data_formatter import format_car_data
from result_formatter import format_results

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/car-check', methods=['POST'])
def car_check():
    number = request.form.get('number')
    fetched_data = fetch_car_data(number)
    return jsonify(results=fetched_data)

@app.route('/run-script', methods=['POST'])
def run_script():
    data = request.get_json()
    query = data['query']

    print(f"Received OSINT query: {query}")  # Отладочное сообщение

    results = fetch_osint_data(query)
    print(f"Raw results from fetch_osint_data: {results}")  # Выводим необработанные результаты

    formatted_results = format_results(results)  # Форматируем результаты

    print(f"OSINT Results found: {formatted_results}")  # Отладочное сообщение

    return jsonify(results=formatted_results)

if __name__ == "__main__":
    app.run(debug=True)
