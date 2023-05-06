from weather_api import *

tempoAnterior = millis()
API()

try:
    while True:
        if millis() - tempoAnterior >= 2760000:  # 46 minutos
            tempoAnterior = millis()
            API()

except KeyboardInterrupt:
    print('C.A.R.I.N.H.A. finalizado')

finally:
    pass
