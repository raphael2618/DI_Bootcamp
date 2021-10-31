class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("nico", 1)
cat2 = Cat("pink", 2)
cat3 = Cat("Foxy", 4)


def dogOld(cat_list):
    cat = sorted(cat_list, key=lambda cat: cat.age)[-1]
    return cat
