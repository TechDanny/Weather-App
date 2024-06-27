from flask import Flask, render_template, request
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv() #loads the .env file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        return render_template('index.html', weather_data=weather_data, title=city)
    return render_template('index.html', weather_data=None)

def get_weather_data(city):
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    weather_data = json.loads(response.text)
    return weather_data

if __name__ == '__main__':
    app.run(debug=True)

