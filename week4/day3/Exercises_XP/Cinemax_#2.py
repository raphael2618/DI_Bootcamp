family = {"rick": 43, 'beth': 13, 'morty': 0, 'summer': 12}
familyValues = family.values()
# print(familyValues)
familyKeys = family.keys()
dict ={}
for (key,value) in family.items():
    if value < 3:
        dict[key] = value
    print(dict)
    # elif value > 3 or value < 12:
    #     ticket = 10
    # elif value > 12:
    #     print(familyKeys, "12")
    #     ticket = 15
