from emotional_rating.weather_api import weather_api
from utils import *

tempoAnterior = millis()
weather_api.get_weather()

try:
    while True:
        if millis() - tempoAnterior >= 2760000:  # 46 minutos
            tempoAnterior = millis()
            weather_api.get_weather()

except KeyboardInterrupt:
    print('C.A.R.I.N.H.A. finalizado')

finally:
    pass
