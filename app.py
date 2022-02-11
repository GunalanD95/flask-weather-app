import requests
from flask import Flask, render_template, request
API_KEY = 'f486f5938741e8cf9f1cd71cdc0d9d37'


app = Flask(__name__)

@app.route('/')
def index():
    """
    Returns the index page
    """
    return render_template('index.html')


def get_weather_res(request,city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid='+API_KEY
    print("url", url)
    get_req = requests.get(url)
    return get_req.json()


if __name__ == '__main__':
    app.run(debug=True)