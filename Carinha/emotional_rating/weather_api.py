from datetime import date
import requests
from utils import json_write
from utils import week_day_list


class WeatherApi():

    def get_weather(self):
        """Queries the weather API and saves relevant data to a JSON file"""

        token = '5pU_kiVDbnaTRqp8feiC0GktoGJ5iOwV0-cPYZ-KZhs'
        coord = '-8.059641978650072,-34.87248963042983' #CESAR School from Recife
        unit = 'metric' #metric = celcius/km
        details = 'true'
        duration = 0 #0 = current, 6 = last 6h, 24 = last 24h
        language = 'pt-BR'

        url_api = f'https://atlas.microsoft.com/weather/currentConditions/json?api-version=1.1'\
            f'&query={coord}'\
            f'&unit={unit}'\
            f'&details={details}'\
            f'&duration={duration}'\
            f'&language={language}'\
            f'&subscription-key={token}'

        response = requests.get(url=url_api, timeout=30).json()['results'][0]

        file_content = {
            'dateTime': response['dateTime'],
            'weekDay': week_day_list[date.weekday(date.today())],
            'weather': response['phrase'],
            'iconCode': response['iconCode'],
            'isDayTime': response['isDayTime'],
            'temperature': response['temperature']['value'],
            'windSpeed': response['wind']['speed']['value']
        }

        json_write('Carinha/emotional_rating/current_data.json', file_content)

weather_api = WeatherApi()
