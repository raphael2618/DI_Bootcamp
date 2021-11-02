class Currency:
    def __init__(self, curr, number):
        self.curr = curr
        self.number = number

    def __str__(self):
        print(f"{self.curr}+ ' ' +{self.number}")

    def __int__(self):
        print(f"{self.number}")

    def __repr__(self):
        print(f"{self.number}{self.curr}")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
