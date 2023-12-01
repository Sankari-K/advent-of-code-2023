DIGITS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def get_puzzle_input(directory):
    """
    Given a directory, parses and returns input as a list
    """
    with open(directory) as f:
        return f.readlines()

def modify_input(lines):
    """
    Given a list of lines, transforms digits into letters for each line
    """
    return [modify_line(line) for line in lines]

def modify_line(line):
    """
    Given a line, eightwothree -> 823
    """
    for word, digit in DIGITS.items():
        # in "eightwothree", replacing "two" with "2" leads to "eigh2three", "eight" can't be found now 
        # fix: replace "two" with "t2o", "three" with "t3e" etc
        line = line.replace(word, word[0] + digit + word[-1])  
    return line
    
def get_calibration_value(line):
    """
    Returns the calibration value for each line
    """
    calibration_value = [value for value in line if value.isdigit()]
    return int(calibration_value[0] + calibration_value[-1]) # "th7th" should give us 77

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
