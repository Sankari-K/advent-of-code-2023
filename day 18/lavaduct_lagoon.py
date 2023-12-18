from matplotlib.path import Path

NEXT = {"U": lambda x, y, a: [(x - i, y) for i in range(1, a + 1)], 
        "D": lambda x, y, a: [(x + i, y) for i in range(1, a + 1)], 
        "L": lambda x, y, a: [(x, y - i) for i in range(1, a + 1)], 
        "R": lambda x, y, a: [(x, y + i) for i in range(1, a + 1)]}

def get_puzzle_input(directory):
    with open(directory) as file:
        return [line.strip().split() for line in file]

def dig_perimeter(DIG_PLAN):
    current = (0, 0)
    coordinates = [current]

    for direction, steps, color in DIG_PLAN:
        current = NEXT[direction](*current, int(steps))
        coordinates.extend(current)
        current = current[-1]

    return coordinates[:-1]

def get_area(path):    
    area = 0
    for i, point in enumerate(path[1:-1], start=1):
        area += point[1] * (path[i - 1][0] - path[i + 1][0])
    area = 0.5 * abs(area)
    return area + 1 - len(path)//2 + len(path)

DIG_PLAN = get_puzzle_input(r"./puzzle_input.txt")
print(get_area(dig_perimeter(DIG_PLAN)))