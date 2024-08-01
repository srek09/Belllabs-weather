import requests
from notifypy import Notify
import time
 

API_KEY = 'your_api_key_here'
CITY = 'Tokyo'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

def get_weather():
    try:
        response = requests.get(URL)
        data = response.json()
        if data['cod'] == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            return f'Temperature: {temperature}°C\nCondition: {description}'
        else:
            return 'Error: Unable to fetch weather data'
    except Exception as e:
        return f'Error: {e}'
 
while True:
    weather_info = get_weather()
    notification = Notify()
    notification.title = 'Current Weather'
    notification.message = weather_info
    notification.send()
    time.sleep(60)
