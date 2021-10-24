from random import sample

message = str(input("Enter a string of 10 characters\n") or "Motivation")
if len(message) < 10:
    print("string not long enough")
elif len(message) > 10:
    print("string too long")

size = len(message)
display = ""
for char in message:
    display += char
    print(display)
randomM = sample(message, size)
print(str(randomM))
