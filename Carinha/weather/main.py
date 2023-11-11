"""Describes the Azure API weather units"""

import csv


class Weather():
    """The weather unit contanier"""

    class WeatherUnit():
        """The weather unit with its order identifier and description"""
        def __init__(self, index, description, *icon_numbers):
            self.index = index
            self.description = description
            self.icon_numbers = icon_numbers

        def __str__(self):
            return f'{self.index} {self.icon_numbers} {self.description}'

        def __sub__(self, other):
            return abs(self.index - other.index)

    def __init__(self, lang='en'):
        self.weathers = self.__create_weathers(lang)

    def __getitem__(self, key):
        for weather_unit in self.weathers:
            if key in weather_unit.icon_numbers:
                return weather_unit

        raise IndexError('climate index out of range')

    def __create_weathers(self, lang):
        weather_units = []

        with open('Carinha/weather/weather_map.csv', encoding='UTF-8') as weather_file:
            weather_reader = csv.DictReader(weather_file)

            text_day = 'lang text day'.replace('lang', lang)

            for index, weather_unit in enumerate(weather_reader):
                icons = [int(weather_unit['icon number day'])]
                if weather_unit['icon number night'] != '':
                    icons.append(int(weather_unit['icon number night']))

                weather_unit = self.WeatherUnit(index, weather_unit[text_day], *icons)
                weather_units.append(weather_unit)

        return weather_units
