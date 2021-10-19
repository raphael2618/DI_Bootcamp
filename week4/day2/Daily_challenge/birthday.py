from datetime import datetime

my_string = input('Enter date(dd-mm-yyyy): ')
# my_date = datetime.strptime(my_string, "%d/%m/%Y")
d = datetime.strptime(my_string, "%d/%m/%Y")
print(d)