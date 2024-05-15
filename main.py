import random
from Deck import Deck

def main():
    #Add 1 and 6
    addition_example = add_two_numbers(1, 6)
    print(addition_example)
    
    #Flip coin
    print(flip_coin())
    
    #Make a deck and print all of the cards in the deck
    the_deck = Deck()
    the_deck.print_deck()
    

def add_two_numbers(num_1, num_2):
    added_nums = num_1 + num_2
    return added_nums

def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        return "heads"
    else:
        return "tails"





if __name__ == "__main__":
    main()
