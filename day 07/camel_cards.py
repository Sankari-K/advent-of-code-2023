from functools import cmp_to_key
from collections import Counter

# the counts of unique characters is distinct and can be used to find the "strength" of the type
# in TYPE_STRENGTHS, higher the element, higher the power 
TYPE_STRENGTHS = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]

def get_puzzle_input(directory):
    with open(directory) as file: 
        return [line.split() for line in file]

def modify_card(hand):
    # Remove joker and replace with best possible cards
    # (replacing joker with the most common card (other that joker ofc) gives us the strongest possible card)
    if hand == "JJJJJ":
        return "11111"
    count_joker = hand.count("J")
    hand = hand.replace("J", "")
    highest_card = Counter(hand).most_common()[0][0]
    return hand + highest_card * count_joker
    
def get_type(hand, joker):
    # identifies and returns the "strength" of the type
    if joker:
        hand = modify_card(hand)
    counter = sorted(Counter(hand).values())
    return TYPE_STRENGTHS.index(counter)

def get_relative_strength(hand1, hand2):
    # check which hand is higher card-wise, left to right
    for a, b in zip(hand1, hand2):
        if CARD_STRENGTHS.index(a) != CARD_STRENGTHS.index(b):
            return CARD_STRENGTHS.index(a) - CARD_STRENGTHS.index(b)
    
def compare_hand(hand1, hand2, joker):
    # if both hands are of different types: check on the basis of types
    # if both hands are of same types: check on the basis of each card  
    if get_type(hand1, joker) != get_type(hand2, joker):
        return get_type(hand1, joker) - get_type(hand2, joker)
    return get_relative_strength(hand1, hand2) 

def get_total_winnings(cards, joker=False):
    cards = sorted(cards, key=cmp_to_key(lambda x, y: compare_hand(x[0], y[0], joker)))
    total_winnings = 0
    for rank, card in enumerate(cards, start=1):
        total_winnings += rank * int(card[1])
    return total_winnings

cards = get_puzzle_input(r"./puzzle_input.txt")

CARD_STRENGTHS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
print(get_total_winnings(cards))

CARD_STRENGTHS = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
print(get_total_winnings(cards, joker=True))