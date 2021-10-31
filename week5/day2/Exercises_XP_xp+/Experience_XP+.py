# Family
class Family:
    __slots__ = ["name", "age", "gender", "is_child"]

    # it's also the Born method
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    F1 = Family = (
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
    )

    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False

    def membersPrint(self):
        for i in Family.F1:
            print(i)


# Theincrediblefamily
class TheIncredibles(Family):
    __slots__ = ["power", "incredible_name"]


    def add(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    add("Jack jack")
