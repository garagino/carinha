"""Describes the Azure API weather units"""

import csv

class Climate():
    """The weather unit contanier"""

    class ClimateUnit():
        """The weather unit with its order identifier and description"""
        def __init__(self, index, description, *icon_numbers):
            self.index = index
            self.description = description
            self.icon_numbers = icon_numbers

        def __str__(self):
            return f'{self.index}\t{self.icon_numbers}    \t{self.description}'

    def __init__(self, lang='en'):
        self.climates = self.__create_climates(lang)

    def __getitem__(self, key):
        for climate in self.climates:
            if key in climate.icon_numbers:
                return climate

        raise IndexError('climate index out of range')

    def __create_climates(self, lang):
        climate_units = []

        with open(r'Carinha\emotional_rating\climate_map.csv', encoding='UTF-8') as climate_file:
            climate_reader = csv.DictReader(climate_file)

            index = 0

            text_day = 'lang text day'.replace('lang', lang)
            #text_night = 'lang text night'.replace('lang', lang)

            for climate_unity in climate_reader:
                icons = [int(climate_unity['icon number day'])]
                if climate_unity['icon number night'] != '':
                    icons.append(int(climate_unity['icon number night']))

                climate = self.ClimateUnit(index, climate_unity[text_day], *icons)
                climate_units.append(climate)
                index += 1

        return climate_units

if __name__ == "__main__":
    c = Climate('pt')
    for i in c.climates:
        print(i)
