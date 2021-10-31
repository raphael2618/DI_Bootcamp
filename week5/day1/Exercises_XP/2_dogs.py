class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print("{} barks ! WAF".format(self.name))

    def jump(self):
        cm = self.height * 2
        print(self.name, "jump ", format(cm))


DavidDogs = Dog("rex", 50)
DavidDogs.bark()
DavidDogs.jump()

sarahs_dog = Dog("Teacup", 20)
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.jump() > DavidDogs.jump():
    print(f"Sarah dog's {sarahs_dog.name} is bigger.")
else:
    print(f"David dog's {DavidDogs.name} is bigger.")
