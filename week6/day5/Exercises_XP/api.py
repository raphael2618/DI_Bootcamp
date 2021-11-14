# Teh database given api is NOT free despite subscription using "https://restcountries.com/" api instead

import psycopg2
import requests
import json
import random

#DB credentials
HOSTNAME = 'localhost'
USERNAME = 'raphael'
PASSWORD = '#'
DATABASE = 'countries'

# db side 'create database countries;'
connection = psycopg2.connect(
    host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE
)

cursor = connection.cursor()

# create the table
try:
    cursor.execute('''
create table countries(
country_id serial primary key,
name varchar(50) not null unique,
capital varchar(50),
flag varchar(50),
subregion varchar(50),
population bigint
);''')
    connection.commit()
except:
    connection.reset()


# get random countries from api
url = requests.get("https://restcountries.com/v3.1/all")
data = json.loads(url.text)
countries = []
randoms = []
for i in range(10):
    ran = random.randint(0, len(data) - 1)
    while ran in randoms:
        ran = random.randint(0, len(data) - 1)
    print(ran)
    randoms.append(ran)
    countries.append(data[ran])

for country in countries:
    try:
        name = country['name']['common'].replace("'", "^")
    except:
        name = 'undefined'
    try:
        capital = list(country['capital'])[0].replace("'", "^")
    except:
        capital = 'undefined'
    try:
        flag = country['flag']
    except:
        flag = 'undefined'
    try:
        subregion = country['subregion'].replace("'", "^")
    except:
        subregion = 'undefined'
    try:
        population = country['population']
    except:
        population = 0

    cursor.execute(f'''
    insert into countries (name, capital, flag, subregion, population)
    values ('{name}', '{capital}', '{flag}', '{subregion}', {population})
    ''')
    connection.commit()

cursor.execute('drop table countries')   # for testing
connection.commit()

connection.close()