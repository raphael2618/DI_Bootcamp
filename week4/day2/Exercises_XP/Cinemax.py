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
        for i in familyTicket:
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
