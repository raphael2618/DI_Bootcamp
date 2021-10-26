import datetime
from pyfiglet import *

cake = '''
   |:H:a:p:p:y:|
 __|___________|__
|^^^^^^^^^^^^^^^^^|
֫|:B:i:r:t:h:d:a:y:|
|                 |
~~~~~~~~~~~~~~~~~~~
'''

name = input("Enter your name")
today = datetime.datetime.now().date()
day, month, year = input("Enter birthdate in the format dd/mm/yyyy: ").split("/")
print("You are born the : ", day, month, year)
diff_time = datetime.date.today() - datetime.date(int(year), int(month), int(day))
UserAge = diff_time.days // 365
print("Your age is :", UserAge)
units = UserAge % 10
num = "_" * ((12 - units) // 2)
print(f"    {num}{units * 'i'}{num}", end='')

print(cake)
msg = 'Happy Birthday'
HB = figlet_format(msg, font='slant')
name = figlet_format(name, font='slant')
print(HB + name)
