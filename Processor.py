from classes.Person import Person

# Based on data from March 11
number_of_infections = 489172
number_of_deaths = 16479
number_of_recoveries = 344267

def get_value_from_block(value : str, block : str):
    return block.split(value)[1].split('\n')[0].strip()

data = open('data/data.txt', "r", encoding='utf-8').read()

people = []

for block in data.split("####"):
    number = get_value_from_block('Number:', block)
    sex = get_value_from_block('Sex:', block)
    age = get_value_from_block('Age:', block)
    chronic_illnesses = get_value_from_block('Chronic illnesses:', block)
    people.append(Person(number, sex, age, chronic_illnesses))

print('0-17: {:.2f}%'.format(len([person.age for person in people if person.age < 18])/len(people)*100))
print('18-44: {:.2f}%'.format(len([person.age for person in people if 18 <= person.age < 45]) / len(people) * 100))
print('45-64: {:.2f}%'.format(len([person.age for person in people if 45 <= person.age < 65])/len(people)*100))
print('65-74: {:.2f}%'.format(len([person.age for person in people if 65 <= person.age < 75])/len(people)*100))
print('75+: {:.2f}%'.format(len([person.age for person in people if 75 <= person.age])/len(people)*100))

print('\n')

print('{:.2f}% férfi'.format(len([person for person in people if person.sex == 'férfi'])/len(people)*100))
print('{:.2f}% nő'.format(len([person for person in people if person.sex == 'nő'])/len(people)*100))