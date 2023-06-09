"""Representation of an emotion"""

from os import listdir
from weather import weather
from utils import json_read, week_day_list as wdl


class Emotions():

    class Emotion():
        """Emotion represented by a set of weather characteristics."""

        def __init__(self, weather_unit, temperature, week_day):
            self.weather_unit = weather_unit
            self.temperature = temperature
            self.week_day = week_day

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

            week_day_dist_a = abs(wdl.index(self.week_day) - wdl.index(other.week_day))
            week_day_dist_b = abs((len(wdl) - wdl.index(self.week_day)) - wdl.index(other.week_day))

            score += min(week_day_dist_a, week_day_dist_b)

            return score

    def __init__(self):
        self.emotions = self.__generate_emotions()

    def __generate_emotions(self):
        emotions_list = []
        path_emotions = 'Carinha/emotional_rating/emotions'
        for file_emotion in listdir(path_emotions):
            dict_file = json_read(f'{path_emotions}/{file_emotion}')

            weather_unit = weather[dict_file['iconCode']]
            temperature = dict_file['temperature']
            week_day = dict_file['weekDay']

            emotions_list.append(self.Emotion(weather_unit, temperature, week_day))

        return emotions_list

    def get_current_data(self):
        """Return a current emotion from a JSON file"""
        weather_data = json_read('Carinha/emotional_rating/current_data.json')

        weather_unit = weather[weather_data['iconCode']]
        temperature = weather_data['temperature']
        week_day = weather_data['weekDay']

        return self.Emotion(weather_unit, temperature, week_day)


emotions = Emotions()
current = emotions.get_current_data()

for emotion in emotions.emotions:
    print(current.compare(emotion))
