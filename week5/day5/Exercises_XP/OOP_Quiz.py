'''A user-defined prototype for an object that defines a set of attributes that characterize any object of the class.
The attributes are data members (class variables and instance variables) and methods, accessed via dot notation. '''

'''An individual object of a certain class. An object obj that belongs to a class Circle, 
for example, is an instance of the class Circle. '''

'''Encapsulation is the packing of data and functions that work on that data within a single object. By doing so, 
you can hide the internal state of the object from the outside. This is known as information hiding. '''

'''Abstraction is used to hide the internal functionality of the function from the users. The users only interact 
with the basic implementation of the function, but inner working is hidden. '''

'''
The transfer of the characteristics of a class to other classes that are derived from it.
'''

'''
A class can be derived one base class in Python.
In multiple inheritance, the features of all the base classes are inherited into the derived class.
'''

'''Polymorphism defines the ability to take different forms. Polymorphism in Python allows us to define methods in 
the child class with the same name as defined in their parent class. '''

'''
how to resolve a method or attribute. MRO is from bottom to top and left to right.
'''




from random import shuffle

class Card:

    available_suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    available_values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, suit, value):
        if suit not in Card.available_suits:
            raise ValueError  # (f"{suit} is not a valid suit.")
        elif str(value) not in Card.available_values:
            raise ValueError  # (f"{value} is not a valid value.")
        else:
            self.suit = suit
            self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)  # f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        # Save each instance of Card to the cards list attribute -- how?
        # Not fully sure about the self.name = name, self.cards = cards naming/meaning?
        # Can set self.cards to a list instead of cards???
        # **Think of these attributes as key: value pairs. See Chicken Coop hard set eggs
        self.cards = [Card(s, v) for v in Card.available_values for s in Card.available_suits]

    def __repr__(self):
        return f"Deck of {self.count()} cards"
        #  "Deck of {} cards".format(len(self.cards))
        #  f"Deck of {len(self.cards)} cards"

    def __iter__(self):
        return iter(self.cards)
    '''
    Once we learn GENERATORS, we can also write it like this:
    def __iter__(self):
        for card in self.cards:
            yield card
    '''
    def reset(self):
        '''Reset the deck back to original init state'''
        self.cards = [Card(s, v) for v in Card.available_values for s in Card.available_suits]
        return self

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        return shuffle(self.cards)  # !!! Forgot to return self.CARDS!!

    def _deal(self, number=1):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        elif self.count() < number:  # Use try/except here?
            print("Only {} cards left. Will deal all remaining cards.".format(self.count()))
            dealt = [self.cards.pop() for x in range(self.count())]
            return dealt[-number:]
        else:
            dealt = [self.cards.pop() for x in range(number)]
            # if len(dealt) == 1:
            #     return dealt[0]  # Returns the single Card instance
            # else:
            return dealt[-number:]  # Returns list of Card instances

    def deal_card(self):
        return self._deal(1)[0]  # Need trick to add [0] to return Card not []. Saves if/else logic in _deal.

    def deal_hand(self, number):
        return self._deal(number)