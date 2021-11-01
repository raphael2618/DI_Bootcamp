'''
1
from datetime import date
def dateOfToday():
    dateOfTodayV = date.today()
    print(dateOfTodayV)

dateOfToday()
'''

'''
2
import datetime
date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
ends = datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
print(timenow - ends)
'''

'''
3
import datetime
timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
deadline = "2021-01-01 00:00:00"
start = datetime.datetime.strptime(timenow,'%Y-%m-%d %H:%M:%S')
ends = datetime.datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')
print(start - ends)
'''

'''
4
import datetime
def dateOfToday():
    dateOfTodayV = datetime.today()
    print(dateOfTodayV)
    dateTimeOfToday = datetime.datetime.today()
    holidayName = "hanouka"
    holidayDate = "2021-11-28 00:00:00"
    nextHoliday = dateTimeOfToday - holidayDate
    print("The next holidays are" + holidayName + " in " + nextHoliday)
    
dateOfToday()
'''


'''
5
from decimal import Decimal
from functools import partial
class SpaceAge:
    _exp = Decimal('1.00')
    _planets = {planet: 31557600 * period for planet, period in {
        'earth': Decimal(1),
        'mercury': Decimal('0.2408467'),
        'venus': Decimal('0.61519726'),
        'mars': Decimal('1.8808158'),
        'jupiter': Decimal('11.862615'),
        'saturn': Decimal('29.447498'),
        'uranus': Decimal('84.016846'),
        'neptune': Decimal('164.79132'),
    }.items()}
    def __init__(self, seconds: int):
        self._seconds = Decimal(seconds)
    def __getattr__(self, key: str):
        planet = key.replace('on_', '')
        if planet in self._planets:
            return partial(self._calc, planet)
        else:
            raise AttributeError(f"No such attribute: {key}")
    def _calc(self, planet: str) -> float:
        return float((self._seconds / self._planets[planet]).quantize(self._exp))
'''

'''
6
from faker import Faker
fake = Faker()
user = {"name":fake.name(), "adress":fake.address(), "language code":fake.language_code()}
print(user)
'''






