brand = {'name': 'Zara', 'creation_date': 1975, 'creator_name': 'Amancio Ortega Gaona',
         'type_of_clothes': {'men', 'women', 'children', 'home'},
         'international_competitors': {'Gap', 'H & M', 'Benetton'},
         'number_stores': 7000,
         'major_color': {'France': 'blue',
                         'Spain': 'red',
                         'US': ('pink', 'green')
                         }
         }

print("Zara is a company created in", brand['creation_date'], "by", brand['creator_name'] + "." +
      "his clothes are for", brand['type_of_clothes'], brand['international_competitors'],
      "his international competitor are :")

brand['number_stores'] = 2

brand['country_creation'] = "Spain"
if brand['international_competitors'] in brand:
    brand['international_competitors'] = "Disigual"

del brand['creation_date']

for i in brand['international_competitors']:
    lenInter = len(brand['international_competitors'])
    print(i[lenInter - 1])

print(brand['major_color']['US'])
print(len(brand))

print(brand.keys())

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

new_brand = brand.update(more_on_zara)


