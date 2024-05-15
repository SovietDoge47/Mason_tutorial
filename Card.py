

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def print_card(self):
        # print(str(self.value) + " of " + self.suit)
        if self.value == 11:
            self.value = "Jack"
        elif self.value == 12:
            self.value = "Queen"
        elif self.value == 13:
            self.value = "King"
        elif self.value == 14:
            self.value = "Ace"
        print(f"{self.value} of {self.suit}")
