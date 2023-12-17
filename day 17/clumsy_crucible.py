import heapq

DIRECTIONS = ["T", "D", "L", "R"]
NEXT = {"T": lambda x, y: (x - 1, y), "D": lambda x, y: (x + 1, y), "L": lambda x, y: (x, y - 1), "R": lambda x, y: (x, y + 1)}
RELATIVE_DIRECTION = {(0, -1): "R", (0, 1): "L", (-1, 0): "D", (1, 0): "T"}

def get_puzzle_input(directory):
    with open(directory) as file:
        file = file.read().split() 

    CITY = dict()
    MAX_X = len(file)   
    MAX_Y = len(file[0])

    for x, line in enumerate(file):
        for y, char in enumerate(line):
            CITY[(x, y)] = int(char)
    return CITY, MAX_X, MAX_Y

def get_min_heat_loss(min_steps, max_steps):
    seen = set()
    queue = [(0, (0, 1), (0, 0), 1), (0, (1, 0), (0, 0), 1)]  # [(loss, current, prev, direction_steps)]

    while queue:
        loss, current, prev, direction_steps = heapq.heappop(queue)

        if prev == (MAX_X - 1, MAX_Y - 1):
            return loss

        # if out of bounds
        if current not in CITY:
            continue
        if (prev, current, direction_steps) in seen:
            continue
        seen.add((prev, current, direction_steps))
    
        for direction in DIRECTIONS:
            next = NEXT[direction](*current)
            prev_direction = RELATIVE_DIRECTION[(prev[0] - current[0], prev[1] - current[1])]

            if next == prev:
                continue
            
            if direction == prev_direction and direction_steps < max_steps:
                heapq.heappush(queue, (loss + CITY[current], next, current, direction_steps + 1))
            elif direction != prev_direction and direction_steps >= min_steps:
                heapq.heappush(queue, (loss + CITY[current], next, current, 1))
  
CITY, MAX_X, MAX_Y = get_puzzle_input(r"./puzzle_input.txt")
print(get_min_heat_loss(1, 3))
print(get_min_heat_loss(4, 10))

