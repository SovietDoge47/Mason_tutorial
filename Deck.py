from Card import Card

class Deck():
    def __init__(self):
        self.cards = []
        self.make_deck()
    
    
    def make_deck(self):
        suits = ["Diamonds", "Spades", "Clubs", "Hearts"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))
    
    def print_deck(self):
        for card in self.cards:
            card.print_card()
    