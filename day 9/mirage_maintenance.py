def get_puzzle_input(directory):
    with open(directory) as file: 
        return [list(map(int, line.split())) for line in file]

def get_difference(history):
    return [b - a for a, b in zip(history, history[1:])]

def get_extrapolated_value(history, forwards):
    if set(history) == {0}:
        return 0
    if forwards:
        return history[-1] + get_extrapolated_value(get_difference(history), forwards)
    return history[0] - get_extrapolated_value(get_difference(history), forwards)

def get_sum_extrapolated_values(REPORT, forwards=True):
    return sum([get_extrapolated_value(history, forwards) for history in REPORT])

REPORT = get_puzzle_input(r"./puzzle_input.txt")
print(get_sum_extrapolated_values(REPORT))
print(get_sum_extrapolated_values(REPORT, False))