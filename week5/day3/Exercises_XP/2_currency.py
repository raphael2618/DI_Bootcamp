class Currency:
    def __init__(self, curr, number):
        self.curr = curr
        self.number = number

    def __str__(self):
        print(f"{self.curr}{self.number}")

    def __int__(self):
        print(f"{self.number}")

    def __repr__(self):
        print(f"{self.number}{self.curr}")

