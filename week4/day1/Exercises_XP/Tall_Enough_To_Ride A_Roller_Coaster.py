#take the height of the user in cm and convert it to inches.
# https://www.rapidtables.com/convert/length/height-converter.html
inchesUser = int(input("How tall are you ? (ieg. 165 for 1 m 65)\n"))
res1 = inchesUser*2.54
res2 = res1/12
res3 = round(res2*12)
print("your tall in inches is", str(res3))
if res3 > 145:
    print("Your are tall enough to ride")
else:
    print("Sorry but you need to grow some more to ride !")
