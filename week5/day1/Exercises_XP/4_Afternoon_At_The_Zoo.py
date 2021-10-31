class Zoo:
    def __init__(self, zoo_Name, animal_list):
        self.zoo_Name = zoo_Name
        self.animal_list = animal_list

    def add_animal(self, animal):
        self.animal_list = []
        self.animal_list.append(animal)

    def get_animals(self):
        for i in self.animal_list:
            return i

    def sell_animal(self,i):
        if i in self.animal_list:
            del i

    def sort_animals(self):
        self.animal_list.sort()

    def get_groups(self):
        print(self.animal_list)



ramat_gan_safari = ["cat", "cougar", "dog", "bear", "emu", "eel"]
print(Zoo.add_animal(ramat_gan_safari))
print(Zoo.get_animals(ramat_gan_safari))
print(Zoo.sell_animal(ramat_gan_safari))
print(Zoo.sort_animals(ramat_gan_safari))
