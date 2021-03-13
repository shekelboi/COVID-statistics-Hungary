from time import sleep
from classes.Person import Person
from bs4 import BeautifulSoup
import requests

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
        #print(person)
        People.append(person)
    sleep(0.2)

file = open("out.txt", "wb")

for person in People:
    file.write(str(str(person) + '\n').encode('utf-8'))
    file.write('####\n'.encode('utf8'))

file.close()

#print(soup.findAll('td', {'class': 'views-field views-field-field-elhunytak-sorszam'}))

# for i in reversed(range(current_last_page + 1)):
#     print(i)
#     sleep(0.1)
