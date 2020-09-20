"""
This package includes the components that make up the war game.

ToDo:

"""

from random import shuffle
from common import constants

class Card():
    """
    Playing card
    ATTRIBUTES:
        suit (__str__r): Suit of card
        rank (str): Card Value
        value (int): numerical value of card
    """

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

    def __int__(self):
        return constants.values[self.rank]

if __name__ == "__main__":
    king_hearts = Card("Hearts","K")
    print(king_hearts)
    print(int(king_hearts))