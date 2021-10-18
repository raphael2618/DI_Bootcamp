while True:

    pizzaTopping = input("Enter your favorite pizza enter  the word quit  when finished\n")
    listPizza = []
    listPizza.append(pizzaTopping)
    while pizzaTopping != "quit":
        pizzaTopping = input("Enter another favorite pizza\n")
        listPizza.append(pizzaTopping)
        price = 10 + 2.5
        if pizzaTopping == "quit":
            listPizza.remove("quit")
    for i in listPizza:
        print("Your pizza is :", str(i), " and his price is : ", str(price))
    if pizzaTopping == "quit":
        quit()
