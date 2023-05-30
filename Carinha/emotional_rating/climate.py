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
            return f'{self.index}\t{self.icon_numbers}    \t{self.description}'

        def __sub__(self, other):
            return abs(self.index - other.index)

    def __init__(self, lang='en'):
        self.weather = self.__create_climates(lang)

    def __getitem__(self, key):
        for weather_unity in self.weather:
            if key in weather_unity.icon_numbers:
                return weather_unity

        raise IndexError('climate index out of range')

    def __create_climates(self, lang):
        weather_units = []

        with open(r'Carinha\emotional_rating\climate_map.csv', encoding='UTF-8') as climate_file:
            weather_reader = csv.DictReader(climate_file)

            text_day = 'lang text day'.replace('lang', lang)
            #text_night = 'lang text night'.replace('lang', lang)

            for index, weather_unity in enumerate(weather_reader):
                icons = [int(weather_unity['icon number day'])]
                if weather_unity['icon number night'] != '':
                    icons.append(int(weather_unity['icon number night']))

                weather_unit = self.WeatherUnit(index, weather_unity[text_day], *icons)
                weather_units.append(weather_unit)

        return weather_units


weather = Weather('pt')



