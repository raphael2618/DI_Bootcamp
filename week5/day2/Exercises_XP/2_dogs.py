class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def bark(self):
        print("{} barks ! WAF".format(self.name))

    def run_speed(self):
        weight_number = self.weight
        age_number = self.age
        speedRun = (weight_number / age_number * 10)
        print("The speed run of the dog is :", speedRun)

    def fight(self, other_dog):
        weight_number = self.weight
        age_number = self.age
        speedRun = (weight_number / age_number * 10)
        winner = speedRun * weight_number
        print(max(winner))


DogDaisy = Dog("daisy", 1, 13)
DogF = Dog("Franc", 2, 15)
DogDonald = Dog("Donald", 2, 15)
