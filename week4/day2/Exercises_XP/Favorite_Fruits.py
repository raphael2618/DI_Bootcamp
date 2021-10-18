fruits = str(input("Which fruits do you love the most ? (ieg. banana,apple)\n")).split(',')
listFruit = []
for i in fruits:
    listFruit.append(i)
    #i'm create a dictionnary of mylist in order to remove all the duplicate
listFruit = list(dict.fromkeys(listFruit))
userFruit = str(input("Choose a fruit "))
if userFruit in listFruit:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")
