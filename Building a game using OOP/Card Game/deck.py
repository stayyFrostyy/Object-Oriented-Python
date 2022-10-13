# Imports Card class
from card import Card
import random

# Defines Deck class
class Deck:
    # Initiates deck object as an empty list
    def __init__(self):
        self.deck = []
        # Adds 52 Card objects to the deck
        for suit in range(4):
            for rank in range(13):
                self.deck.append(Card(suit, rank))
        
        self.shuffle()

    # Creates method to check length of deck (list)
    def __len__(self):
        return len(self.deck)

    # Creates method to add a card to the deck
    def add_card(self, card):
        self.deck.append(card)

    # Creates method to return the last card in Deck
    def pop_card(self):
        return self.deck.pop()

    def shuffle(self):
        random.shuffle(self.deck)