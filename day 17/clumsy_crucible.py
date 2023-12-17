import heapq

DIRECTIONS = ["T", "D", "L", "R"]

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

def get_next(current, direction):
    x, y = current  
    if direction == "T":
        return (x - 1, y)
    if direction == "D":
        return (x + 1, y)
    if direction == "L":
        return (x, y - 1)
    return (x, y + 1)

def get_relative_direction(prev, current):
    x, y = current
    if prev == (x, y - 1):
        return "R"
    if prev == (x, y + 1):
        return "L"
    if prev == (x - 1, y):
        return "D"
    return "T"

def get_min_heat_loss():
    seen = set()
    queue = [(0, (0, 1), (0, 0), 1), (0, (1, 0), (0, 0), 1)]

    while queue:
        loss, current, prev, direction_steps = heapq.heappop(queue)

        # if current is the destination (bottom-right)
        # if current == (MAX_X - 1, MAX_Y - 1):
        #     return loss

        # if out of bounds
        if current not in CITY:
            continue
        if (prev, current, direction_steps) in seen:
            continue
        seen.add((prev, current, direction_steps))
    
        for direction in DIRECTIONS:
            next = get_next(current, direction)
            if next == prev:
                continue

            if direction == get_relative_direction(prev, current) and direction_steps < 3:
                if next == (MAX_X - 1, MAX_Y - 1):
                    return loss + CITY[(MAX_X - 1, MAX_Y - 1)] + CITY[current]

                heapq.heappush(queue, (loss + CITY[current], next, current, direction_steps + 1))
            elif direction != get_relative_direction(prev, current):
                if get_next(current, direction) == (MAX_X - 1, MAX_Y - 1):
                    return loss + CITY[(MAX_X - 1, MAX_Y - 1)]
                heapq.heappush(queue, (loss + CITY[current], next, current, 1))
  
CITY, MAX_X, MAX_Y = get_puzzle_input(r"./puzzle_input.txt")
print(get_min_heat_loss())
