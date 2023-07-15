"""CARINHA

Emotive robotics artifact capable of expressing emotions based on climate and environmental data.

This is a project by GARAGino, Research Group on Physical Computing at CESAR School
"""

from emotional_rating.weather_api import weather_api
from emotional_rating.emotion import emotions
from breathing import breathe


def main():
    """Starts CARINHA threads"""

    weather_api.start()
    breathe.start()

    print(emotions.get_current_emotion())

if __name__ == '__main__':
    main()
