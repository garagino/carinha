"""

    Representation of an emotion

"""

from os import listdir
import weather
import utils


class EmotionalRating():
    """
        List of Emotions

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

            self_emotion_index = utils.wdl.index(self.week_day)
            other_emotion_index = utils.wdl.index(other.week_day)
            week_day_distance_a = abs(self_emotion_index - other_emotion_index)
            week_day_distance_b = abs((len(utils.wdl) - self_emotion_index) - other_emotion_index)

            score = 0
            score += self.weather_unit - other.weather_unit
            score += abs(self.temperature - other.temperature)
            score += min(week_day_distance_a, week_day_distance_b)

            return score
        
    def __init__(self):
        self.emotions = self.__generate_emotions()
        self.weather = weather.Weather('pt')

    def __generate_emotions(self):
        """Generates a list of emotions from reference files"""

        reference_files = listdir(utils.EMOTIONS_DIR)
        
        emotions_list = []
        for file_emotion in reference_files:
            file_dictonary = utils.json_read(utils.EMOTIONS_DIR + file_emotion)

            name = file_dictonary['name']
            weather_unit = self.weather[file_dictonary['iconCode']]
            temperature = file_dictonary['temperature']
            week_day = file_dictonary['weekDay']

            emotions_list.append(self.Emotion(name, weather_unit, temperature, week_day))

        return emotions_list

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
    
    def __get_current_data(self):
        """Return a current emotion data from a JSON weather file"""

        weather_data = utils.json_read(utils.WEATHER_DIR + utils.CURRENT_DATA_FILE)

        weather_unit = self.weather[weather_data['iconCode']]
        temperature = weather_data['temperature']
        week_day = weather_data['weekDay']

        return self.Emotion('current', weather_unit, temperature, week_day)
