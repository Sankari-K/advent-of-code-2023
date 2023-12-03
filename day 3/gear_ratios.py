from collections import defaultdict
from functools import reduce

def parse_puzzle_input(directory):
    with open(directory) as f:
        lines = f.read().split("\n")
    
    for line_num, line in enumerate(lines):
        parse_line(line + ".", line_num)

def parse_line(line, line_num):
    current_number = ""
    for x, char in enumerate(line):
        if char.isdigit():
            current_number += char
        elif current_number:
            NUMBERS[current_number].append([x - len(current_number), x - 1, line_num])
            current_number = ""

        if char != "." and not(char.isdigit()):
            SYMBOLS.add((x, line_num))
        if char == "*":
            STARS.add((x, line_num))

def check_part_number(number, coordinate):
    start_x, end_x, y = coordinate
    adjacent_cells = [(start_x - 1, y), (end_x + 1, y)] + [(x, y + 1) for x in range(start_x - 1, end_x + 2)] + [(x, y - 1) for x in range(start_x - 1, end_x + 2)]
    
    for adjacent_cell in adjacent_cells:
        if adjacent_cell in STARS:
            STARS[adjacent_cell].add(int(number))
    
    for adjacent_cell in adjacent_cells:
        if adjacent_cell in SYMBOLS:
            return 1
    return 0
        
def check_part_numbers(coordinates, number):
    return sum([check_part_number(number, coordinate) for coordinate in coordinates])

def sum_part_numbers(NUMBERS):
    sum = 0
    for number, coordinates in NUMBERS.items():
        sum += int(number) * check_part_numbers(coordinates, number) 
    return sum

def get_gear_ratio():
    sum = 0
    for adjacent in STARS.values():
        if len(adjacent) == 2:
            sum += reduce(lambda x, y: x * y, adjacent)
    return sum

NUMBERS = defaultdict(list)  # "34": [(start_x, end_x, y), (start_x, end_x, y)]
SYMBOLS = set()  # {(x, y), (x, y)}
STARS = set()    # {(x, y), (x, y)}

parse_puzzle_input(r"./puzzle_input.txt")   # assign values to NUMBERS, SYMBOLS, STARS 
STARS = {star: set() for star in STARS} 

print(sum_part_numbers(NUMBERS))
print(get_gear_ratio())
