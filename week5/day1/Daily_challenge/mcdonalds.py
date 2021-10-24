class Farm:
    def __init__(self):
        self.animals = []

    def add(self, animal):
        self.animals.append(animal)

    def __str__(self):
        s = ''
        for animal in self.animals:
            s += 'Old MacDonald had a farm, EE-I-EE-I-O,\n'
            s += 'And on that farm he had a ' + animal.name + ', EE-I-EE-I-O,\n'
            s += 'With a ' + animal.noise * 2 + ' here and a '  + animal.noise * 2 +' there\n'
            s += 'Here a ' + animal.noise + ', there a ' + animal.noise + ', everywhere a '+ animal.noise * 2 + '\n'
        s += 'Old MacDonald had a farm, EE-I-EE-I-O.\n'
        return s

class Animal:
    def __init__(self, name, noise):
        self.name = name
        self.noise = noise


farm = Farm()
farm.add(Animal('cow', 'moo'))
print(farm)
farm.add(Animal('duck', 'kwak'))
farm.add(Animal('dog', 'woof'))
farm.add(Animal('cat', 'miaoo'))
print(farm)
def verse():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")


def sing(animal, noise):
    sound = tuple([noise] * 8)
    verse()
    print("And on that farm he had a %s, Ee-igh, Ee-igh, Oh!" % animal)
    print("With a %s, %s here and a %s, %s there.\n\
Here a %s, there a %s, everywhere a %s, %s." % sound)
    verse()


def main():
    sing("cow", "moo")
    print(sing("horse", "neigh"))
    print(sing("pig", "oink"))
    print(sing("goat", "baa"))
    print(sing("hen", "cluck"))


main()

