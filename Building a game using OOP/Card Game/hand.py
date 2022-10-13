# Imports Deck Class
from deck import Deck

class Hand(Deck):
    # Sub-Class Inherits all of Deck's methods
    # Override __init__ from Deck Class
    def __init__(self, label):
        self.deck = []
        self.label = label
        self.win_count = 0

    def __str__(self):
        return self.label + ': ' + ''.join([str(card) for card in self.deck])
