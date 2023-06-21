"""Representation of an emotion"""

from os import listdir
from emotional_rating.weather import weather
from utils import json_read, week_day_list as wdl


class Emotions():
    """List of Emotions

    Instantiate a list of emotions from reference files.
    Generates a reference to current emotions and defines which emotion is being felt now.
    """

    class Emotion():
        """Emotion represented by a set of weather characteristics."""

        def __init__(self, name, weather_unit, temperature, week_day):
            self.name = name
            self.weather_unit = weather_unit
            self.temperature = temperature
            self.week_day = week_day

        def __str__(self):
            return f'{self.name} [{self.weather_unit} {self.temperature}]'

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
        """Generates a list of emotions from reference files"""

        emotions_list = []
        path_emotions = 'Carinha/emotional_rating/emotions'
        for file_emotion in listdir(path_emotions):
            dict_file = json_read(f'{path_emotions}/{file_emotion}')

            name = dict_file['name']
            weather_unit = weather[dict_file['iconCode']]
            temperature = dict_file['temperature']
            week_day = dict_file['weekDay']

            emotions_list.append(self.Emotion(name, weather_unit, temperature, week_day))

        return emotions_list

    def __get_current_data(self):
        """Return a current emotion data from a JSON weather file"""

        weather_data = json_read('Carinha/emotional_rating/current_data.json')

        weather_unit = weather[weather_data['iconCode']]
        temperature = weather_data['temperature']
        week_day = weather_data['weekDay']

        return self.Emotion('current', weather_unit, temperature, week_day)

    def get_current_emotion(self):
        """Returns the current emotion

        Compares current weather data with each predefined emotion

        Returns
        -------
        Emotion
            Returns closest emotion.
        """

        current_data = self.__get_current_data()
        emotions_score = {}

        for emotion in self.emotions:
            emotions_score[emotion] = current_data.compare(emotion)

        return min(emotions_score, key=emotions_score.get)


emotions = Emotions()

current_emotion = emotions.get_current_emotion()
print(current_emotion)
