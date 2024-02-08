import requests
import os
from twilio.rest import Client

api_key = os.environ.get('OWM_API_KEY')
account_sid = 'AC9c457b1e7cc3036f10ad5c3a7401dacf'
auth_token = '0303a1d7c8351fc8873cb53d255ca2f8'

openweather_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'

lat = 50.937531
lon = 6.960279

weather_params = {
    'lat': lat,
    'lon': lon,
    'cnt': 4,
    'appid': api_key
}

response = requests.get(openweather_endpoint, params=weather_params)
data = response.json()

weather_ids_list = []

for num in range(0, 4):
    weather_id = data['list'][num]['weather'][0]['id']
    weather_ids_list.append(weather_id)

if any(id < 700 for id in weather_ids_list):
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrella",
        from_='+1234567890',
        to='+491234567889'
    )
    print(message.status)
