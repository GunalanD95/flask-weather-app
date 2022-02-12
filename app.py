import requests
import datetime
from flask import Flask, render_template, request
API_KEY = 'f486f5938741e8cf9f1cd71cdc0d9d37'


app = Flask(__name__)

@app.route('/')
def index():
    """
    Returns the home page
    """
    return render_template('home.html')

@app.route('/results',methods=['POST']) 
def get_weather_res():
    now = datetime.datetime.now()
    dayName = now.strftime("%A")
    Month = now.strftime("%d , %B ")
    city_name = request.form['cityName']

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid='+API_KEY+'&units=metric'
    print("url", url)
    get_req = requests.get(url)
    content = get_req.json()

    weather = content['weather'][0]['main']
    temp = content['main']['temp']
    name = content['name']
    return render_template('index.html', city_name= name,weather= weather,temp= temp,dayName= dayName,Month= Month)

if __name__ == '__main__':
    app.run(debug=True)