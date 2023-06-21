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

        #Link de chamada da API
        api = f'https://atlas.microsoft.com/weather/currentConditions/json?api-version=1.1'\
            f'&query={coord}'\
            f'&unit={unit}'\
            f'&details={details}'\
            f'&duration={duration}'\
            f'&language={language}'\
            f'&subscription-key={token}'

        # Usa a biblioteca 'requests' para pegar os dados da API e transforma num arquivo json
        dados = requests.get(url=api, timeout=30).json()['results'][0]

        # Dicionario com todos os dados
        file = {
            'dateTime': dados['dateTime'],
            'weekDay': week_day_list[date.weekday(date.today())],
            'weather': dados['phrase'],
            'iconCode': dados['iconCode'],
            'isDayTime': dados['isDayTime'],
            'temperature': dados['temperature']['value'],
            'windSpeed': dados['wind']['speed']['value']
        }

        # Função que transforma dicionario em arquivo json
        json_write('Carinha/emotional_rating/current_data.json', file)

weather_api = WeatherApi()
