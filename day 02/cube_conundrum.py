from collections import defaultdict
from functools import reduce

MAXIMUM = {"red": 12, "green": 13, "blue": 14}

def get_puzzle_input(directory):
    """
    Given a directory, returns a list of games, where a game is a dictionary like MAXIMUM
    """
    with open(directory) as f:
        lines = f.readlines()
    
    games = [line.split(": ")[1].strip() for line in lines]
    return [get_formatted_game(game) for game in games]

def get_formatted_game(game):
    """
    Given a game ('3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'), returns a dictionary like MAXIMUM
    of maximum balls picked of each color
    """
    game = game.replace("; ", ", ").split(", ")
    formatted_game = defaultdict(lambda: 0)
    for pick in game:
        pick = pick.split()
        formatted_game[pick[1]] = max(formatted_game[pick[1]], int(pick[0]))
    return formatted_game

def sum_of_gameid(games):
    ans_a, ans_b = 0, 0
    for id, game in enumerate(games, start=1):
        if is_possible(game):
            ans_a += id
        ans_b += lowest_possible(game)
    return ans_a, ans_b

def is_possible(game):
    """
    Returns whether a particular game is possible given the maximum balls available
    """
    return all([MAXIMUM[color] >= game[color] for color in MAXIMUM])

def lowest_possible(game):
    """
    Returns the minimum "power" of balls required to play a game
    """
    return reduce(lambda x, y: x * y, game.values())

games = get_puzzle_input(r"./puzzle_input.txt")
print(sum_of_gameid(games))  # (part a, part b)