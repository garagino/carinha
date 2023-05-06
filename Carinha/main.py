from weather_api import *

tempoAnterior = millis()
get_weather()

try:
    while True:
        if millis() - tempoAnterior >= 2760000:  # 46 minutos
            tempoAnterior = millis()
            get_weather()

except KeyboardInterrupt:
    print('C.A.R.I.N.H.A. finalizado')

finally:
    pass
