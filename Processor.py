from classes.Person import Person
from datetime import datetime
import os
from bs4 import BeautifulSoup
import requests

DATA_FOLDER = 'data'
TXT_EXTENSION = '.txt'


# Based on data from March 11

def today():
    return "{0}-{1}-{2}".format(datetime.now().year, datetime.now().month, datetime.now().day)


STATISTICS = os.path.join(DATA_FOLDER, 'Statistics (' + today() + ')' + TXT_EXTENSION)


def get_value_from_block(value: str, block: str):
    return block.split(value)[1].split('\n')[0].strip()


def percentage_calculator(arr1, arr2, ratio_only=False):
    ratio = len(arr1) / len(arr2)
    if ratio_only:
        return ratio
    else:
        return ratio * 100


try:
    with open(STATISTICS) as file:
        number_of_infections = int(file.readline().replace(',', ''))
        number_of_deaths = int(file.readline().replace(',', ''))
        number_of_recoveries = int(file.readline().replace(',', ''))
except FileNotFoundError:
    with open(STATISTICS, 'w') as file:
        worldometer = BeautifulSoup(requests.get('https://www.worldometers.info/coronavirus/country/hungary/').text,
                                    'html.parser')
        elements = worldometer.findAll('div', {'class': 'maincounter-number'})
        statistics = [e.text.strip().replace(',', '') for e in elements]
        number_of_infections = int(statistics[0])
        number_of_deaths = int(statistics[1])
        number_of_recoveries = int(statistics[2])
        file.write('\n'.join(statistics))

print(today() + TXT_EXTENSION)

data = open('data/data.txt', "r", encoding='utf-8').read()

people = []

for block in data.split("###"):
    number = get_value_from_block('Number:', block)
    sex = get_value_from_block('Sex:', block)
    age = get_value_from_block('Age:', block)
    chronic_illnesses = get_value_from_block('Chronic illnesses:', block)
    people.append(Person(number, sex, age, chronic_illnesses))

print('0-17: {:.2f}%'.format(percentage_calculator([person.age for person in people if person.age < 18], people)))
print(
    '18-44: {:.2f}%'.format(percentage_calculator([person.age for person in people if 18 <= person.age < 45], people)))
print(
    '45-64: {:.2f}%'.format(percentage_calculator([person.age for person in people if 45 <= person.age < 65], people)))
print(
    '65-74: {:.2f}%'.format(percentage_calculator([person.age for person in people if 65 <= person.age < 75], people)))
print('75+: {:.2f}%'.format(percentage_calculator([person.age for person in people if 75 <= person.age], people)))

print('\n')

print('{:.2f}% férfi'.format(percentage_calculator([person for person in people if person.sex == 'férfi'], people)))
print('{:.2f}% nő'.format(percentage_calculator([person for person in people if person.sex == 'nő'], people)))

print('\n')

print('Felépült: {:.2f}%'.format(number_of_recoveries / number_of_infections * 100))
print('Aktív esetek: {:.2f}%'.format(
    (number_of_infections - number_of_recoveries - number_of_deaths) / number_of_infections * 100))
print('Halálozás: {:.2f}%'.format(number_of_deaths / number_of_infections * 100))

print('Halálozás megoszlása életkor szerint:')

for i in range(0, 106):
    victims = [person for person in people if person.age == i]
    print('{0}: {1:.3f}%'.format(i, percentage_calculator(victims, people)))