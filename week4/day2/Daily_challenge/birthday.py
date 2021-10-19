

cake ='''
|:H: a:p: p:y: |
__ | ___________ | __________________
| ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |
|:B: i:r: t:h: d:a: y: |
| |                 |  |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

import datetime
today = datetime.datetime.now().date()
day, month, year = input("Enter birthdate in the format dd/mm/yyyy: ").split("/")
print("You are born the : ", day, month, year)
YearUSer = int(year)
todayD = datetime.date.today()
UserAge = todayD.year - YearUSer
print("Your age is :", UserAge)
units = UserAge % 10

print(units * "i")
for letter in cake:
    print(letter, end='')