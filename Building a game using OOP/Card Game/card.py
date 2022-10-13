
# Defines Card Class
class Card:
    suits = ['\u2666', '\u2665', '\u2663', '\u2660']
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    # Initiates Object with a suit and a rank from arguments - ETC: 4 Hearts
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # Creates string reference to object
    def __str__(self):
        return f"{Card.ranks[self.rank]}{Card.suits[self.suit]}"