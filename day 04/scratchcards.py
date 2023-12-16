from math import floor

def get_puzzle_input(directory):
    scratchcards = []
    with open(directory) as file:    
        for line in file:
            card = []
            line = line.split(": ")[1].split(" | ")
            for winning_numbers in line:
                card.append(set(winning_numbers.split()))
            scratchcards.append(card)
    return scratchcards

def find_matches(card):
    return len(card[0].intersection(card[1]))
               
def find_game_points(card):
    return floor(2 ** (find_matches(card) - 1))

def find_total_points(scratchcards):
    return sum([find_game_points(scratchcard) for scratchcard in scratchcards])

def find_total_scratchcards(scratchcards):
    number_scratchcards = dict()
    matches = dict()

    for index, scratchcard in enumerate(scratchcards, start=1):
        matches[index] = find_matches(scratchcard)
        number_scratchcards[index] = 1

    for scratchcard in range(1, len(scratchcards) + 1):
        for match in range(scratchcard + 1, scratchcard + matches[scratchcard] + 1):
            number_scratchcards[match] += number_scratchcards[scratchcard]
    return sum(number_scratchcards.values())


scratchcards = get_puzzle_input(r"./puzzle_input.txt")
print(find_total_points(scratchcards))
print(find_total_scratchcards(scratchcards))
