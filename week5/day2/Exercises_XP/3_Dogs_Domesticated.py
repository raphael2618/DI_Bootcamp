sys.path.append(".")
from dogs.py import Dog()
class PetDog(Dog):
    def __init__(self, trained ):
        self.trained  = trained

