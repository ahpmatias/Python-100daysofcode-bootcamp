# This file covers the challenge of day 38 from the course "100 days of code", by Dr. Angela Yu, provided by Udemy.
import os
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

api_key = os.environ.get('API_KEY')
app_id = os.environ.get('APP_ID')
sheety_user = os.environ.get('SHEETY_USER')
sheety_password = os.environ.get('SHEETY_PASSWORD')


# Endpoint to get natural language data for exercise
nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# Endpoint to Sheety
sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')

nutritionix_headers = {
    'Content-Type': 'application/json',
    'x-app-id': app_id,
    'x-app-key': api_key
}

query = input('Which exercise did you do today?: ')

params = {
    'query': query,
}

nutritionix_response = requests.post(url=nutritionix_endpoint, json=params, headers=nutritionix_headers)
data = nutritionix_response.json()

# sheety_get_response = requests.get(url=sheety_endpoint)
# sheety_data = sheety_get_response.json()
# print(sheety_data)

sheety_params = {
    'workout': {
        'date': datetime.now().strftime('%d/%m/%Y'),
        'time': datetime.now().strftime('%X'),
        'exercise': data['exercises'][0]['name'],
        'duration': data['exercises'][0]['duration_min'],
        'calories': data['exercises'][0]['nf_calories'],
    }
}

sheety_post_response = requests.post(url=sheety_endpoint, json=sheety_params, auth=(sheety_user, sheety_password))
