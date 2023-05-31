"""Representation of an emotion"""


from os import listdir
from weather import weather
from weather_api import weather_api


class Emotions():

    class Emotion():
        """Emotion represented by a set of weather characteristics."""

        def __init__(self, weather_unit, temperature):
            self.weather_unit = weather_unit
            self.temperature = temperature

        def __str__(self):
            return f'{self.weather_unit}\t{self.temperature}'

        def compare(self, other):
            """Returns a score, which is the sum of the differences between emotions.
            
            Parameters
            ----------
            other : Emotion
                Emotion to be compared
            
            Returns
            -------
            int
                The lower the returned value, the more similar the emotions are.
            """
            score = 0

            score += self.weather_unit - other.weather_unit
            score += abs(self.temperature - other.temperature)

            return score

        '''def read_from_file(self):
            """Return a emotion from a JSON file"""
            weather_data = json_read('Carinha/weather_data.json')

            weather_unit = weather_data['iconCode']
            temperature = weather_data['temperature']

            return Emotion(weather[weather_unit], temperature)'''

    def __init__(self):
        print(self.__generate_emotions())

    def pega(self):
        return self.__generate_emotions()

    def __generate_emotions(self):
        emotions = []
        path_emotions = r'Carinha\emotional_rating\emotions'
        for file_emotion in listdir(path_emotions):
            dict_file = weather_api.json_read(f'{path_emotions}\\{file_emotion}')
            emotions.append(self.Emotion(dict_file['iconCode'], dict_file['temperature']))

        return emotions
            

e = Emotions()
for em in e.pega():
    print(em)

'''alegria = Emotion(weather[1], 28.5)
tristeza = Emotion(weather[18], 20.0)

atual = Emotion(weather[1], 0.0)
atual = atual.read_from_file()

print(atual.compare(alegria))
print(atual.compare(tristeza))
'''