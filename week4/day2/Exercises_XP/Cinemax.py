while True:
    familyTicket = int(input("What is the age of the member?"))
    listFamilyTicket = []
    listFamilyTicket.append(familyTicket)
    strContinue = str(input("Have you another member ? (Y/N)"))
    while strContinue == "Y":
        familyTicket = int(input("What is the age of the other member?"))
        # listFamilyTicket.append(familyTicket)
        listFamilyTicket.append(familyTicket)
        strContinue = str(input("Have you another member ? (Y/N)"))
    if strContinue == "N":
        for i in listFamilyTicket:
            totalTicketSum = 0
            if i < 3:
                totalTicket = 0
            elif i > 3 or i < 12:
                totalTicket = 10
            elif familyTicket > 12:
                totalTicket = 15
            familyTicket = int(input("Enter the age of each person for you wants tickets enter quit when finished"))
            totalTicket = totalTicket * totalTicket
            print("The ticket total is :", totalTicket)
    prompt = "How old are you?"
    prompt += "\nEnter 'quit' when you are finished. "

    while True:
        age = input(prompt)
        if age == 'quit':
            break
        age = int(age)

        if age < 3:
            print("  You get in free!")
        elif age < 13:
            print("  Your ticket is $10.")
        else:
            print("  Your ticket is $15.")

