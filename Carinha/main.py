from emotional_rating.weather_api import weather_api
from utils import millis
from emotional_rating.emotion import emotions

tempoAnterior = millis()
weather_api.get_weather()

try:
    while True:
        if millis() - tempoAnterior >= 2760000:  # 46 minutos
            tempoAnterior = millis()
            weather_api.get_weather()
            current_emotion = emotions.get_current_emotion()
            print(current_emotion)      


except KeyboardInterrupt:
    print('C.A.R.I.N.H.A. finalizado')

finally:
    pass
