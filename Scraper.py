from datetime import datetime
from time import sleep
from classes.Person import Person
from bs4 import BeautifulSoup
import requests
import os

base_url = "https://koronavirus.gov.hu/elhunytak?page="
current_last_page = 329  # Goes until 0

People = []

for page_number in reversed(range(current_last_page + 1)):
    url = base_url + str(page_number)
    print(url)
    page = requests.get(url).text

    soup = BeautifulSoup(page, 'html.parser')

    for tr in reversed(soup.findAll('tr')[1:]):
        data = tr.findAll('td')
        number = data[0].text.strip()
        sex = data[1].text.strip()
        age = data[2].text.strip()
        chronic_illnesses = data[3].text.strip()
        person = Person(number, sex, age, chronic_illnesses)
        People.append(person)
    sleep(0.1)

directory = 'data'
file_name = "{0}-{1}-{2}.txt".format(datetime.now().year, datetime.now().month, datetime.now().day)
file = open(os.path.join(directory, file_name), "wb")


def fix_encoding(text: str):
    text = text.replace('õ', 'ő')
    text = text.replace('ũ', 'ű')
    text = text.replace('Õ', 'Ő')
    text = text.replace('Ũ', 'Ű')
    return text


delimiter = '###'

output = ("\n" + delimiter + "\n").join([str(person) for person in People])

output = fix_encoding(output)

file.write(output.encode('utf-8'))

file.close()

# print(soup.findAll('td', {'class': 'views-field views-field-field-elhunytak-sorszam'}))

# for i in reversed(range(current_last_page + 1)):
#     print(i)
#     sleep(0.1)
