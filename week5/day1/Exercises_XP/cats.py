class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("nico", 1)
cat2 = Cat("pink", 2)
cat3 = Cat("Foxy", 4)


def dogOld(c1, c2, c3):
    cats = [c1.age, c2.age, c3.age]
    return max(cats)


print(f"The oldest cat is {dogOld(cat1, cat2, cat3)} years old")
