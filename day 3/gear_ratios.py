from collections import defaultdict
from functools import reduce

def get_puzzle_input(directory):
    NUMBERS = defaultdict(list)  # "34": [(start_x, end_x, y), (start_x, end_x, y)]
    SYMBOLS = set()  # {(x, y), (x, y)}
    STARS = set()

    with open(directory) as f:
        lines = f.read().split("\n")
    
    for line_num, line in enumerate(lines):
        numbers, symbols, stars = parse_line(line, line_num)
        SYMBOLS = SYMBOLS.union(symbols)
        STARS = STARS.union(stars)
        NUMBERS = update_numbers(NUMBERS, numbers)

    return NUMBERS, SYMBOLS, STARS

def update_numbers(NUMBERS, numbers):
    for number in numbers:
        NUMBERS[number].extend(numbers[number])
    return NUMBERS

def parse_line(line, line_num):
    numbers = defaultdict(list)
    symbols = set()
    stars = set()

    current_number = ""
    for x, char in enumerate(line):
        if char.isdigit():
            current_number += char
        elif current_number:
            numbers[current_number].append([x - len(current_number), x - 1, line_num])
            current_number = ""

        if char != "." and not(char.isdigit()):
            symbols.add((x, line_num))
        if char == "*":
            stars.add((x, line_num))

    if current_number:
        numbers[current_number].append([len(line) - len(current_number) - 1, len(line) - 2, line_num])
    return numbers, symbols, stars

def check_part_number(number, coordinate):
    start_x, end_x, y = coordinate
    adjacent_cells = [(start_x - 1, y), (end_x + 1, y)] + [(x, y + 1) for x in range(start_x - 1, end_x + 2)] + [(x, y - 1) for x in range(start_x - 1, end_x + 2)]
    
    for adjacent_cell in adjacent_cells:
        if adjacent_cell in STARS:
            STARS[adjacent_cell].add(int(number))
    
    for adjacent_cell in adjacent_cells:
        if adjacent_cell in SYMBOLS:
            return True
    return False
        
def check_part_numbers(number, coordinates):
    occurance = 0
    for coordinate in coordinates:
        if check_part_number(number, coordinate):
            occurance += 1
    return occurance

def sum_part_numbers(NUMBERS):
    sum = 0
    for number, coordinates in NUMBERS.items():
        sum += int(number) * check_part_numbers(number, coordinates) 
    return sum

def get_gear_ratio():
    sum = 0
    for adjacent in STARS.values():
        if len(adjacent) == 2:
            sum += reduce(lambda x, y: x * y, adjacent)
    return sum

NUMBERS, SYMBOLS, STARS = get_puzzle_input(r"./puzzle_input.txt")
STARS = {star: set() for star in STARS}
print(sum_part_numbers(NUMBERS))
print(get_gear_ratio())
