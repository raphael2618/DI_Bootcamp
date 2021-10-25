class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class SnowBall(Cat):
    def sing(self, sound):
        return f'{sound}'

my_cats = [Simon('Simon',4), Sally('Sally',5), SnowBall('SnowBall',3)]

my_pets = Pets(my_cats)

my_pets.walk()

