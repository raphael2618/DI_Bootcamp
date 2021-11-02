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

    def __iadd__(self, other):
        print(f"{self.number}{self.curr}")
        if type(other) == int:
            print(f"{self.number}{other}")
        elif type(other) == int or type(self.number) == int:
            print(self.number + other)
        elif self.curr != other:
            raise TypeError('Can not add cirrencies together !')


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
