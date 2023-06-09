import json
from time import time

def millis():
    """Returns the current time in milliseconds"""

    return int(time() * 1000)

def json_read(arquivo):
    try:
        with open (arquivo, 'r') as file:
            dados = json.load(file)
        return dados
    except:
        print('There was an error opening the file')

def json_write(json_object):
    try:
        with open('Carinha/emotional_rating/current_data.json', 'w') as outfile:
            outfile.write(json_object)
    except:
        print('An error occurred while creating the file')

week_day_list = ['Monday',
                 'Tuesday',
                 'Wednesday',
                 'Thursday',
                 'Friday',
                 'Saturday',
                 'Sunday']
