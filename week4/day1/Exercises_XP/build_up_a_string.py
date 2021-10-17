import random
from random import sample
message  = str(input("Enter a string of 10 characters\n") or "Motivation")
if len(message) < 10:
    print("string not long enough")
elif len(message) > 10:
    print("string too long")

print(message[0])
size = len(message)
print(message[size-1])
display = ""
for char in message:
    display += char
    print(display)
randomM = sample(message,size)
# str(randomM)
#randomMessage = random.shuffle(message)
print(str(randomM))

