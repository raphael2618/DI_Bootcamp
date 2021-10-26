family = {}
quitAnswer = "Y"
while True:
    names = input("Enter a name")
    age = input("Enter a age")
    family = names
    family = age
    if input('Do You Want To Continue? (y/n)') != 'y':
        break

for ageValue in family:
    family[age] = eval(ageValue)
sumCount = 0
if ageValue < 3:

    totalTicket = 0
    sumCount = sumCount + 1
elif ageValue > 3 or ageValue < 12:

    totalTicket = 10
    sumCount = sumCount + 1
elif ageValue > 12:

    totalTicket = 15
    sumCount = sumCount + 1
print(totalTicket * sumCount)
