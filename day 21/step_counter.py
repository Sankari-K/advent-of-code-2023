import math

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_puzzle_input(directory):
    with open(directory) as file:
        file = file.read().split("\n")

    GARDEN = dict()
    for x, line in enumerate(file):
        for y, char in enumerate(line):
            GARDEN[(x, y)] = char
            if char == "S":
                START = (x, y)
    return GARDEN, START

def get_plots(steps, START):
    MAX_X, MAX_Y = max(GARDEN)[0] + 1, max(GARDEN)[1] + 1

    queue = [START]
    
    for _ in range(steps):
        new_queue = set()
        while queue:
            plot = queue.pop()
            for direction in DIRECTIONS:
                next = ((plot[0] + direction[0]) % MAX_X, (plot[1] + direction[1]) % MAX_Y)
                if GARDEN[next] != "#":
                    new_queue.add((plot[0] + direction[0], plot[1] + direction[1]))
        queue = list(new_queue)

    return len(queue)
            
def get_more_plots(START):
    height = max(GARDEN)[0] + 1
    # mod = 26501365 % height
    # seen = list()
    # for times in [mod, mod + height, mod + height * 2]:
    #     seen.append(get_plots(times, START))
    x0, x1, x2 = [3832, 33967, 94056]
    a = (x2 - x0) // 2 - (x1 - x0)
    b = (x1 - x0) - a
    c = x0
    n = math.ceil(26501365 // height)
    return a * n ** 2 + b * n + c


GARDEN, START = get_puzzle_input(r"./puzzle_input.txt")
print(get_plots(64, START))
print(get_more_plots(START))
