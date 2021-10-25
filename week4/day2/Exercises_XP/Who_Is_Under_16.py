list = ["raphael", "samuel", "fayga", "jeremie"]
lenghtList = len(list)
for i in range(lenghtList):
    userAge = int(input("Enter your age"))
    if userAge < 16:
        list.pop(i)
        continue
    print(list)
