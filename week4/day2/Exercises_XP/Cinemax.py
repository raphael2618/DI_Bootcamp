totalTicket = 0
while True:

    familyTicket = int(input("What is the age of the member?"))
    # listFamilyTicket.append(familyTicket)
    counter=0
    if 16 < familyTicket < 21:
        counter+=1

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