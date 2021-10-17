list = []
for i in range(1500, 25001):
    if i % 7 == 0 or i % 5 == 0:
        list.append(str(i))
print(','.join(list))
