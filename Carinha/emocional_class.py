from enum import Enum

class Emotion(Enum):
    FELICIDADE = 1
    TRISTEZA = 2
    RAIVA = 3
    MEDD = 5

class Inputs(Enum):
    DAY_TIME = 1
    WEEK_DAY = 2
    INTERACIONS = 3
    WEATHER = 4
    TEMPERATURE = 5
    # AUDIO = 6
    # PROXIMITY = 7


class Carinha:
    def __init__(self, emotion: Emotion = None):
        self.emotion = emotion
        self.inputs = dict()
        self.score = dict()

    def set_inputs(self, day_time:int, week_day:int, interactions:int,  weather:int, temperature:float):
        import datetime
        self.inputs[Inputs.DAY_TIME] = day_time
        self.inputs[Inputs.WEEK_DAY] = week_day
        self.inputs[Inputs.INTERACIONS] = interactions 
        self.inputs[Inputs.WEATHER] = weather 
        self.inputs[Inputs.TEMPERATURE] = temperature
        
    
    def calculate_score(self, templates):
        # for template in templates:
        #     score = 0
        #     for inputs in template.inputs:
        #         if template.inputs[inputs] >= 3:
        #             score += abs(abs(self.inputs[inputs] - template.inputs[inputs]) - 5)
        
        # self.score[template.inputs] = score
        pass
    
    def intensify(self):
        pass

    
