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

def get_min_heat_loss(current, prev, direction_steps, seen):
    # if current is the destination (bottom-right)
    if current == (MAX_X - 1, MAX_Y - 1):
        return CITY[current]
    # if out of bounds
    if current not in CITY:
        return float('inf')
    if (prev, current, direction_steps) in seen:
        return float('inf')
    
    seen.add((prev, current, direction_steps))
    
    ans = float('inf')
    for direction in DIRECTIONS:
        if get_next(current, direction) == prev:
            continue
        if direction == get_relative_direction(prev, current) and direction_steps < 3:
            ans = min(get_min_heat_loss(get_next(current, direction), current, direction_steps + 1, seen), ans)
        elif direction != get_relative_direction(prev, current):
            ans = min(get_min_heat_loss(get_next(current, direction), current, 1, seen), ans)

    seen.remove((prev, current, direction_steps))
    return CITY[current] + ans
  
CITY, MAX_X, MAX_Y = get_puzzle_input(r"./input.txt")
print(get_min_heat_loss((0, 1), (0, 0), 1, seen=set()))
print(get_min_heat_loss((1, 0), (0, 0), 1, seen=set()))
