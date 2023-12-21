from collections import deque

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
    queue = deque([START])
    
    for _ in range(steps):
        new_queue = deque()
        while queue:
            plot = queue.popleft()
            for direction in DIRECTIONS:
                next = (plot[0] + direction[0], plot[1] + direction[1])
                if next in GARDEN and GARDEN[next] == "." and next not in new_queue:
                    new_queue.append(next)
        queue = new_queue
    return len(queue) + 1
            

GARDEN, START = get_puzzle_input(r"./puzzle_input.txt")
print(get_plots(64, START))