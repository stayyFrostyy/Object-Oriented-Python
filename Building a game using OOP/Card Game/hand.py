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
        return self.label + ': ' + ' '.join([str(card) for card in self.deck])

    # Creates get method for label (players hand)
    def get_label(self):
        return self.label

    # Creates get method for win_count
    def get_win_count(self):
        return self.win_count

    # Adds 1 to win_count when player wins
    def round_winner(self):
        self.win_count += 1