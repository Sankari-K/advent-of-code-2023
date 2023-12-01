DIGITS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def get_puzzle_input(directory):
    """
    Given a directory, this function reads the input and returns it as a list
    """
    with open(directory) as f:
        return f.read().split("\n")

def modify_input(puzzle):
    """
    Given a list of lines, it transforms digits into letters for each line
    """
    new_puzzle = []
    for line in puzzle:
        new_puzzle.append(modifiy_line(line))
    return new_puzzle

def modifiy_line(line):
    """
    Given a line, eightwothree -> 823
    """
    new_line = line[:]
    for word, digit in DIGITS.items():
        new_line = new_line.replace(word, word[0] + digit + word[-1])
    return new_line
    
def get_calibration_value(line):
    """
    Returns the calibration value for each line
    """
    calibration_value = [value for value in line if value.isdigit()]
    return int(calibration_value[0] + calibration_value[-1])

def get_sum_calibration_value(lines):
    """
    Returns the sum of calibration values of all lines
    """
    return sum([get_calibration_value(line) for line in lines])

# part a
puzzle_input = get_puzzle_input(r"./puzzle_input.txt")
print(get_sum_calibration_value(puzzle_input))

# part b
puzzle_input = modify_input(get_puzzle_input(r"./puzzle_input.txt"))
print(get_sum_calibration_value(puzzle_input))
