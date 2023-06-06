import json
from datetime import date
import requests
from utils import json_write
from utils import week_day_list


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
            'weekDay': week_day_list[date.weekday(date.today())],
            'weather': weather,
            'iconCode': icon_code,
            'isDayTime': is_day_time,
            'temperature': temp,
            'windSpeed': wind_speed
        }

        # Função que transforma dicionario em arquivo json
        json_object = json.dumps(file, indent=4)

        json_write(json_object)

weather_api = WeatherApi()
