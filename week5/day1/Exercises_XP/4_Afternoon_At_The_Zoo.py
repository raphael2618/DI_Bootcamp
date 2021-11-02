class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if not new_animal in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):

        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):

        animals_lists = []

        for animal in sorted(self.animals):

            if not animals_lists:
                animals_lists.append([animal])

            else:

                if animal[0] == animals_lists[-1][0][0]:

                    animals_lists[-1].append(animal)
                else:
                    animals_lists.append([animal])


        animals_sorted = {}
        for index, sublist in enumerate(animals_lists):

            if len(sublist) == 1:
                animals_sorted[index + 1] = sublist[0]
            else:
                animals_sorted[index + 1] = sublist

        print(animals_sorted)


ramat_gan_safari = Zoo('Ramat Gan Safari')
for animal in ['Cat', 'Cougar', "Baboon", 'Eel', 'Emu', "Baboon", "Baboon", "Baboon", "Bear", "Ape", ]:
    ramat_gan_safari.add_animal(animal)

ramat_gan_safari.sort_animals()