list = ["raphael", "samuel", "fayga", "jeremie"]
# lenghtList = len(list)
for i in list:
    userAge = int(input("Enter a number"))
    if userAge < 16:
        ageUserRm = str(userAge[i])
        list.remove(ageUserRm)
