import requests
from notifypy import Notify
import time
 
# Your API key (replace with your own)
API_KEY = '71da0e7d8aaf19ad1cf9f59c8c53ce19'
# City for which you want the weather data
CITY = 'Tokyo'
# URL to fetch the weather data
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
 
# Function to get weather data
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
    # Get weather information
    weather_info = get_weather()
    # Create a notification
    notification = Notify()
    notification.title = 'Current Weather'
    notification.message = weather_info
    notification.send()
    # Wait for 1 hour before updating the weather info
    time.sleep(60)
