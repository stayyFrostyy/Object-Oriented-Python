from deck import Deck
from hand import Hand

deck = Deck()
hands = []
for i in range(1, 5):
    hands.append(Hand(f"P{i}"))

while len(deck) > 0:
    for hand in hands:
        hand.add_card(deck.pop_card())


for hand in hands:
    print(hand)
