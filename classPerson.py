class Person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    def introduce(self):
        print( f"I go by the name {self.name} aged {self.age} and am {self.gender}")
person=Person("kelly", 20, "male")

person.introduce()
