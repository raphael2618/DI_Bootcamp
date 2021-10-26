users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
new_user = dict(zip(users, range(len(users))))
print(new_user)

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
new_user = dict(zip(range(len(users)),users))
print(new_user)

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
new_user = dict(zip(range(len(users)),sorted(users)))
print(new_user)

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
letterI="i"
users2 = []
for word in users:
    if letterI in word:
        users2.append(word)
        print(users2)

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
letterP="p"
letterM="m"
users2 = []
for sub in users:
    temp = sub.split()
    for ele in temp:
        if ele[0].lower() == letterP.lower() or ele[0].lower() == letterM.lower():
            users2.append(ele)
print(users2)