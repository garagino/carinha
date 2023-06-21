"""CARINHA

Emotive robotics artifact capable of expressing emotions based on climate and environmental data.

This is a project by GARAGino, Research Group on Physical Computing at CESAR School
"""

from emotional_rating.weather_api import weather_api
from emotional_rating.emotion import emotions
from utils import millis

tempoAnterior = millis()
weather_api.get_weather()
print(emotions.get_current_emotion())

try:
    while True:
        if millis() - tempoAnterior >= 2760000:  # 46 minutos
            tempoAnterior = millis()
            weather_api.get_weather()
            print(emotions.get_current_emotion())

except KeyboardInterrupt:
    print('C.A.R.I.N.H.A. finalizado')

finally:
    pass
