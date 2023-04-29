import requests

token = '5pU_kiVDbnaTRqp8feiC0GktoGJ5iOwV0-cPYZ-KZhs' #Define a chave de acesso da API
coord = '-8.059641978650072,-34.87248963042983' #Define a coordenada que vamos usar
unit = 'metric' # Define a unidade de medida dos dados. metric = celcius/km
details = 'true' # Da mais detalhes sobre o clima, se for falso só retorna o clima predominante
duration = 0 # 0 = atual, 6 = ultimas 6h, 24 = ultimas 24h
language = 'pt-BR' #idioma do clima predominante

api = f'https://atlas.microsoft.com/weather/currentConditions/json?api-version=1.1&query={coord}&unit={unit}&details={details}&duration={duration}&language={language}&subscription-key={token}' #Link de chamada da API 

dados = requests.get(url=api).json() # Usa a biblioteca 'requests' para pegar os dados da API e transforma num arquivo json

# dados da API que vamos utilizar:
clima = dados['results'][0]['phrase'] # A "frase" do clima atual
iconCode = dados['results'][0]['iconCode'] # # Codigo do icone, pode nos ser útil
isDayTime = dados['results'][0]['isDayTime'] # Retorna true se estiver de dia
temperatura = dados['results'][0]['temperature']['value'] # A temperatura em Celcius
velocidade_vento = dados['results'][0]['wind']['speed']['value'] # A veliodcidade do vento em km/h

print(dados['results'][0]['dateTime'])
print(clima)
print(iconCode)
print(isDayTime)
print(temperatura)
print(velocidade_vento)
