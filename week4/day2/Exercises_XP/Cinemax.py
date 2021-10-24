totalTicket = 0
while True:

    familyTicket = int(input("What is the age of the member?"))
    # listFamilyTicket.append(familyTicket)

    if familyTicket < 3:
        totalTicket += 0
    elif familyTicket > 3 or familyTicket < 12:
        totalTicket += 10
    elif familyTicket > 12:
        totalTicket += 15
    Continue = input("Do u want to add another member ? (y/n)")
    if Continue == "y":
        continue
    print("The price is :", totalTicket)

    # prompt = "How old are you?"
    # prompt += "\nEnter 'quit' when you are finished. "
    #
    # while True:
    #     age = input(prompt)
    #     if age == 'quit':
    #         break
    #     age = int(age)
    #
    #     if age < 3:
    #         print("  You get in free!")
    #     elif age < 13:
    #         print("  Your ticket is $10.")
    #     else:
    #         print("  Your ticket is $15.")
