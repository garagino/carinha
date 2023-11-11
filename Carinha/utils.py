"""Utility Functions"""

import sys
import json
from time import time


EMOTIONS_DIR = 'Carinha/emotional/emotions/'
WEATHER_DIR = 'Carinha/emotional/weather/'
CURRENT_DATA_FILE = 'current_data.json'
LOG_TIME_FILE = 'log_time_file.csv'

week_day_list = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

def millis():
    """Returns the current time in milliseconds"""

    return int(time() * 1000)

def json_read(file_path):
    """Returns a dictionary from a read json file."""

    try:
        file = open(file_path, 'r', encoding='UTF-8')
    except OSError:
        print(f'Could not read file: "{file_path}"')
        sys.exit()
    with file:
        return json.load(file)

def json_write(file_path, content):
    """Writes a json object into a file."""

    try:
        json_object = json.dumps(content, indent=4)
        outfile = open(file_path, 'w', encoding='UTF-8')
    except TypeError:
        print(f'Could not serialize content: {content}')
        sys.exit()
    except OSError:
        print(f'Could not write file: {file_path}')
        sys.exit()
    with outfile:
        outfile.write(json_object)
