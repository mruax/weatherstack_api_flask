import os
from requests import request

API_KEY = os.environ.get("API_KEY")


def get_weather(query=''):
    if not query:
        query = 'fetch:ip'
    response = request(
        method='GET',\
        url='http://api.weatherstack.com/current',
        params={
            'access_key': API_KEY,
            'query': query
        }
    )
    if response.status_code == 200:
        return {
            'icon': response.json()['current']['weather_icons'][0],
            'temperature': response.json()['current']['temperature'],
            'feelslike': response.json()['current']['feelslike'],
            'wind_speed': response.json()['current']['wind_speed'],
            'wind_degree': response.json()['current']['wind_degree'],
            'wind_dir': response.json()['current']['wind_dir'],
            'cloudcover': response.json()['current']['cloudcover'],
            'pressure': response.json()['current']['pressure'],
            'precip': response.json()['current']['precip'],
            'humidity': response.json()['current']['humidity'],
            'visibility': response.json()['current']['visibility'],
            'query_name': response.json()['request']['query'],
            'query_type': response.json()['request']['type']
        }