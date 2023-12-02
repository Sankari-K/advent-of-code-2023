from collections import defaultdict

MAXIMUM = {"red": 12, "green": 13, "blue": 14}

def get_puzzle_input(directory):
    """
    Given a directory, returns a list of games, where a game is a list of sets, and a set is a dictionary like MAXIMUM
    """
    with open(directory) as f:
        lines = f.readlines()
    
    games = [line.split(": ")[1].strip() for line in lines]
    return [get_formatted_game(game) for game in games]

def get_formatted_game(game):
    """
    Given a game ('3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'), returns a list of sets, and a set is a dictionary like MAXIMUM
    """
    game = game.split("; ")
    return [get_formatted_set(set) for set in game]

def get_formatted_set(set):
    """
    Given a set, returns it in a representation like MAXIMUM
    """
    set = set.split(", ")
    formatted_set = defaultdict(int)
    for pick in set:
        pick = pick.split()
        formatted_set[pick[1]] = int(pick[0])
    return formatted_set

def sum_of_gameid(games):
    ans_a = 0
    ans_b = 0
    for index, game in enumerate(games, start=1):
        if is_possible(game):
            ans_a += index
        ans_b += lowest_possible(game)
    return ans_a, ans_b

def is_possible(game):
    """
    Returns whether a particular game is possible given the maximum balls available
    """
    for set in game:
        for color in MAXIMUM:
            if MAXIMUM[color] < set[color]:
                return False
    return True

def lowest_possible(game):
    """
    Returns the minimum "power" of balls required to play a game
    """
    power = 1
    for color in MAXIMUM:
        power *= max([set[color] for set in game])
    return power

games = get_puzzle_input(r"./puzzle_input.txt")
print(sum_of_gameid(games))  # (part a, part b)