from emotional_rating.weather_api import weather_api

tempoAnterior = weather_api.millis()
weather_api.get_weather()

try:
    while True:
        if weather_api.millis() - tempoAnterior >= 2760000:  # 46 minutos
            tempoAnterior = weather_api.millis()
            weather_api.get_weather()

except KeyboardInterrupt:
    print('C.A.R.I.N.H.A. finalizado')

finally:
    pass
