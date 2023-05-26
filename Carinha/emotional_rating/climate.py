"""Describes the Azure API weather units"""

import csv

class Climate():
    """The weather unit with its order identifier and description"""

    def __init__(self, index, description, *icon_numbers):
        self.index = index
        self.description = description
        self.icon_numbers = icon_numbers

def create_climates(lang = 'en'):
    climates = []

    with open(r'Carinha\emotional_rating\climate_map.csv', encoding='UTF-8') as climate_file:
        climate_reader = csv.DictReader(climate_file)

        i = 0

        text_day = 'lang text day'.replace('lang', lang)
        #text_night = 'lang text night'.replace('lang', lang)

        for climate_unity in climate_reader:
            icons = [int(climate_unity['icon number day'])]
            if climate_unity['icon number night'] != '':
                icons.append(int(climate_unity['icon number night']))

            climate = Climate(i, climate_unity[text_day], *icons)
            climates.append(climate)
            i += 1

    return climates

if __name__ == "__main__":
    #c = Climate(1, 'description', 1, 2, 3)
    print(locals())
    climates = create_climates('pt')
    for c in climates:
        print(c.index,  c.icon_numbers, c.description)
