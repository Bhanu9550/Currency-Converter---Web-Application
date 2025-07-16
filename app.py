from flask import Flask, render_template, request, jsonify
import os
import requests

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  

app = Flask(__name__)

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/About')
def about():
    return render_template('About.html')

@app.route('/convert')
def convert():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = float(request.args.get('amount'))

    try:
        # Fetch exchange rates
        response = requests.get(f'{BASE_URL}{from_currency}')
        data = response.json()
        
        if data['result'] == 'error':
            return jsonify({'error': data['error-type']})

        rate = data['conversion_rates'][to_currency]
        converted_amount = round(amount * rate, 2)
        
        return jsonify({
            'converted_amount': converted_amount,
            'rate': rate
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)