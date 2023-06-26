"""CARINHA

Emotive robotics artifact capable of expressing emotions based on climate and environmental data.

This is a project by GARAGino, Research Group on Physical Computing at CESAR School
"""

from emotional_rating.weather_api import weather_api
from emotional_rating.emotion import emotions


weather_api.start()
print(emotions.get_current_emotion())
