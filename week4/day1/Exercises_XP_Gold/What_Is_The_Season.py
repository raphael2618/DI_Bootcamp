number = int(input("Enter a number between 1 to 12 for month."))
if number <1 or number>12:
    print("invalid number ! Try again")
    input("Enter a number between 1 to 12 for month.")
else:
    if 3 >= number <= 5:
        print("Spring")
    elif 6 >= number <= 8:
        print("Summer")
    elif 9 >= number <= 11:
        print("Autumn")
    elif 12 >= number <= 2:
        print("Winter")

