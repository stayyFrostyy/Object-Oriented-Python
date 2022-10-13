from card import Card
from deck import Deck

c1 = Card(0, 0)
c2 = Card(1, 1)

deck = Deck()
print(len(deck))

print(c1, c2)
print(c1 < c2)