"""
    CARINHA

    Emotive robotics artifact capable of expressing emotions based on climate and environmental data.

    This is a project by GARAGino, Research Group on Physical Computing at CESAR School
"""

from emotional import EmotionalRating
from breathing import Breathing
from weather import WeatherAPI
from sensor import PresenceSensor


def main():
    """Starts CARINHA threads"""

    weather_api = WeatherAPI()
    weather_api.start()

    breathing = Breathing(led_pin=8, frequency=0.02)
    breathing.start()

    emotions = EmotionalRating()
    print(emotions.get_current_emotion())

if __name__ == '__main__':
    main()
