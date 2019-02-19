import datetime

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def calculate_age(self):
        age_minus_hundred = 100 - self.age
        current_date = datetime.datetime.now()
        current_year = current_date.year
        self.future_year = current_year + age_minus_hundred

    def disply_age(self):
        print("Hi "+self.name+". By Year "+str(self.future_year)+". your age will be 100")


name = input()

age = int(input());

p1 = Person(name,age)

p1.calculate_age()

p1.disply_age()

