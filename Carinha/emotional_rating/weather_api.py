import json
from time import time
import requests


class WeatherApi():

    def get_weather(self):
        """Queries the weather API and saves relevant data to a JSON file"""

        token = '5pU_kiVDbnaTRqp8feiC0GktoGJ5iOwV0-cPYZ-KZhs' # Define a chave de acesso da API
        coord = '-8.059641978650072,-34.87248963042983' # Define a coordenada que vamos usar
        unit = 'metric'  # Define a unidade de medida dos dados. metric = celcius/km
        details = 'true' # Da mais detalhes sobre o clima, se for falso só retorna o clima predominante
        duration = 0  # 0 = atual, 6 = ultimas 6h, 24 = ultimas 24h
        language = 'pt-BR'  # idioma do clima predominante

        # Link de chamada da API
        api = f'https://atlas.microsoft.com/weather/currentConditions/json?api-version=1.1'\
            f'&query={coord}'\
            f'&unit={unit}'\
            f'&details={details}'\
            f'&duration={duration}'\
            f'&language={language}'\
            f'&subscription-key={token}'

        # Usa a biblioteca 'requests' para pegar os dados da API e transforma num arquivo json
        dados = requests.get(url=api).json()

        # dados da API que vamos utilizar:
        weather = dados['results'][0]['phrase']  # A "frase" do clima atual
        # Codigo do icone, pode nos ser útil
        icon_code = dados['results'][0]['iconCode']
        # Retorna true se estiver de dia
        is_day_time = dados['results'][0]['isDayTime']
        # A temperatura em Celcius
        temp = dados['results'][0]['temperature']['value']
        # A veliodcidade do vento em km/h
        wind_speed = dados['results'][0]['wind']['speed']['value']
        date_time = dados['results'][0]['dateTime']

        # Dicionario com todos os dados
        file = {
            'dateTime': date_time,
            'weather': weather,
            'iconCode': icon_code,
            'isDayTime': is_day_time,
            'temperature': temp,
            'windSpeed': wind_speed
        }

        # Função que transforma dicionario em arquivo json
        json_object = json.dumps(file, indent=4)

        self.json_write(json_object)

    def millis(self):
        """Returns the current time in milliseconds"""

        return int(time() * 1000)

    def json_read(self, arquivo):
        try:
            with open (arquivo, 'r') as file:
                dados = json.load(file)
            return dados
        except:
            print('There was an error opening the file')

    def json_write(self, json_object):
        try:
            with open('Carinha/emotional_rating/current_data.json', 'w') as outfile:
                outfile.write(json_object)
        except:
            print('An error occurred while creating the file')

weather_api = WeatherApi()