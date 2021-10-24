while True:
    try:
        number = int(input("First number\n"))
        number2 = int(input("Second number\n"))
        operator = input("Operator : (* / + -)")
        if isinstance(number, int) or isinstance(number2, int):
            if number == number2:
                print(number ** number2)
                break
            elif operator == "*":
                number3 = number * number2
                print(number3)
                break
            elif operator == "+":
                number3 = number + number2
                print(number3)
                break
            elif operator == "-":
                number3 = number - number2
                print(number3)
                break
            elif operator == "/":
                number3 = number / number2
                print(number3)
                break

    except:
        print("Wrong input")
        continue
# else:
#     print("Enter a valid number !")
#     number = int(input("First number\n"))
#     number2 = int(input("Second number\n"))