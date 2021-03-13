class Person:
    def __init__(self, number, sex, age, chronic_illnesses):
        self.number = int(number)
        self.sex = sex
        self.age = int(age)
        self.chronic_illnesses = chronic_illnesses

    def __str__(self):
        return "Number: {0}\nSex: {1}\nAge: {2}\nChronic illnesses: {3}".format(self.number, self.sex, self.age, self.chronic_illnesses)