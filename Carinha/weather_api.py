import requests


def API():
    import json

    # Define a chave de acesso da API
    token = '5pU_kiVDbnaTRqp8feiC0GktoGJ5iOwV0-cPYZ-KZhs'
    # Define a coordenada que vamos usar
    coord = '-8.059641978650072,-34.87248963042983'
    unit = 'metric'  # Define a unidade de medida dos dados. metric = celcius/km
    # Da mais detalhes sobre o clima, se for falso só retorna o clima predominante
    details = 'true'
    duration = 0  # 0 = atual, 6 = ultimas 6h, 24 = ultimas 24h
    language = 'pt-BR'  # idioma do clima predominante

    # Link de chamada da API
    api = f'https://atlas.microsoft.com/weather/currentConditions/json?api-version=1.1&query={coord}&unit={unit}&details={details}&duration={duration}&language={language}&subscription-key={token}'

    # Usa a biblioteca 'requests' para pegar os dados da API e transforma num arquivo json
    dados = requests.get(url=api).json()

    # dados da API que vamos utilizar:
    clima = dados['results'][0]['phrase']  # A "frase" do clima atual
    # Codigo do icone, pode nos ser útil
    iconCode = dados['results'][0]['iconCode']
    # Retorna true se estiver de dia
    isDayTime = dados['results'][0]['isDayTime']
    # A temperatura em Celcius
    temperatura = dados['results'][0]['temperature']['value']
    # A veliodcidade do vento em km/h
    velocidade_vento = dados['results'][0]['wind']['speed']['value']
    dateTime = dados['results'][0]['dateTime']

    arq = {'dateTime': dateTime, 'clima': clima, 'iconCode': iconCode, 'isDayTime': isDayTime,
           'temperatura': temperatura, 'velocidade_vento': velocidade_vento}  # Dicionario com todos os dados

    # Função que transforma dicionario em arquivo json
    json_object = json.dumps(arq, indent=4)

    # Cria um arquivo do tipo Json e configura-o para o modo de escrita (w)
    with open('clima.json', 'w') as outfile:
        outfile.write(json_object)  # Escreve o json dentro do arquivo


def millis():
    from time import time

    milli = int(time() * 1000)
    return milli
