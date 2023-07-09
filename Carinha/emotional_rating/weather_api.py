from time import sleep
from datetime import date
from threading import Thread
import requests
from utils import json_write, week_day_list as wdl
from decouple import config


class WeatherApi(Thread):

    def __init__(self):
        Thread.__init__(self)

    def get_weather(self):
        """Queries the weather API and saves relevant data to a JSON file"""

        token = config('TOKEN')
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
            'weekDay': wdl[date.weekday(date.today())],
            'weather': response['phrase'],
            'iconCode': response['iconCode'],
            'isDayTime': response['isDayTime'],
            'temperature': response['temperature']['value'],
            'windSpeed': response['wind']['speed']['value']
        }

        json_write('Carinha/emotional_rating/emotions/current_data.json', file_content)

    def run(self):
        while True:
            self.get_weather()
            sleep(2760) # 46 minutes

weather_api = WeatherApi()
