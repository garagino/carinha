from API_clima import *

tempoAnterior = millis()
dadosAPI = API()

print(dadosAPI)
try:
    while True:
        if millis() - tempoAnterior >= 2760000: # 46 minutos
            tempoAnterior = millis()
            dadosAPI = API()
            print(dadosAPI)

except KeyboardInterrupt:
    print('C.A.R.I.N.H.A. finalizado')

finally:
    pass

        





