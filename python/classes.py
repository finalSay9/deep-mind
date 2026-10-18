
class Person:
    #class attributes
    name = 'evan'
    age = 24
    address = 'akoma street 241'

    def __init__(self, village, marital_status):
        self.village = village
        self.marital_status = marital_status
Person.name = "Ankoma"
Person.address = "Los Angels"


object1 = Person('Lilongwe', 'married')
print(object1.name, object1.age, object1.address)
print(object1.village, object1.marital_status)
print(Person.name, Person.age, Person.address)
