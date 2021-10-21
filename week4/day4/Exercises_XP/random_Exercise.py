import random
def numberRandom():
    number_random = random.randint(1,101)
    number_random2 = random.randint(1,101)
    if number_random2==number_random:
        print(f"The number {number_random} and {number_random2} are the same. YOU WIN !")
    else:
        print(f"The number {number_random} and {number_random2} are not the same ou fail ! LOSER")

numberRandom()
