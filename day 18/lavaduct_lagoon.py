NEXT = {"U": lambda x, y, a: (x - a, y), "D": lambda x, y, a: (x + a, y), "L": lambda x, y, a: (x, y - a), "R": lambda x, y, a: (x, y + a)}
DIRECTION = {"0": "R", "1": "D", "2": "L", "3": "U"}

def get_puzzle_input(directory):
    with open(directory) as file:
        return [line.strip().split() for line in file]
    
def modify_dig_plan(DIG_PLAN, modify):
    if not modify:
        return [[direction, steps] for direction, steps, color in DIG_PLAN]
    
    for index, plan in enumerate(DIG_PLAN):
        hexdecimal = plan[-1].removeprefix("(#").removesuffix(")")
        DIG_PLAN[index] = [DIRECTION[hexdecimal[-1]], int(hexdecimal[:-1], 16)] # [[direction0, steps0], [direction1, steps1]]
    return DIG_PLAN

def dig_boundary(DIG_PLAN):
    current = (0, 0)
    coordinates = [current]

    for direction, steps in DIG_PLAN:
        current = NEXT[direction](*current, int(steps))
        coordinates.append(current)

    return coordinates

def get_lava_capacity(path):   
    area, path_pts = 0, 0

    for a, b in zip(path, path[1:]):
        area += (a[0] * b[1]) - (a[1] * b[0])
        path_pts += abs(a[0] - b[0]) + abs(a[1] - b[1])

    area = abs(area // 2)
    interior_pts = area + 1 - path_pts // 2
    return interior_pts + path_pts

DIG_PLAN = modify_dig_plan(get_puzzle_input(r"./puzzle_input.txt"), modify=False)
print(get_lava_capacity(dig_boundary(DIG_PLAN)))

DIG_PLAN = modify_dig_plan(get_puzzle_input(r"./puzzle_input.txt"), modify=True)
print(get_lava_capacity(dig_boundary(DIG_PLAN)))