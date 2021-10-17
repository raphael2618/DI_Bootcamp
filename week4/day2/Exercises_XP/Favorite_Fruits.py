fruits = [str(x) for x in input("Which fruits do you love the most ?\n").split(', ')]
listFruit = [fruits]
userFruit = str(input("Choose a fruit "))
#if str equal to list then :
for i in listFruit:
    if userFruit in listFruit:
        print("You chose one of your favorite fruits! Enjoy!")
    else:
        print("You chose a new fruit. I hope you enjoy")
