from card import Card
from deck import Deck
from hand import Hand

deck = Deck()

hand = Hand("Player")
hand.add_card(deck.pop_card())
print(hand)
