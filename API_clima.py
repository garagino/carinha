import requests
from datetime import datetime

key = '454798564a45acb8f030f5f0d4e62678' #Define a chave de acesso da API
coordenada = {'lat': '-8.059641978650072', 'lon': '-34.87248963042983'} #Define a coordenada que vamos usar

api = f"https://api.openweathermap.org/data/2.5/weather?lat={coordenada['lat']}&lon={coordenada['lon']}&appid={key}&units=metric&lang=pt_br" #Link de chamada da API


dados = requests.get(url=api).json() # Usa a biblioteca 'requests' para pegar os dados da API e transforma num arquivo json

# dados da API que vamos utilizar:
climaGeral = dados['weather'][0]['main']
idClimaGeral = dados['weather'][0]['id'] # Todos as descrições de clima tem um ID, podemos usa-lo
horaAtual = datetime.now().strftime('%H:%M') # Pega o horario atual
temperatura = dados['main']['temp'] # Pega a temperatura já em graus Celcius
velVento = dados['wind']['speed'] # Velocidade do vento em metros/segundo

print(climaGeral)
print(idClimaGeral)
print(horaAtual)
print(temperatura)
print(velVento)




