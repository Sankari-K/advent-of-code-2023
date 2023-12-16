from collections import deque

DIRECTIONS = {"-": {"T": ["L", "R"], "D": ["L", "R"], "L": ["R"], "R": ["L"]},
              "|": {"T": ["D"], "D": ["T"], "L": ["T", "D"], "R": ["T", "D"]},
              ".": {"T": ["D"], "D": ["T"], "L": ["R"], "R": ["L"]},
              "/": {"T": ["L"], "D": ["R"], "L": ["T"], "R": ["D"]},
              "\\": {"T": ["R"], "D": ["L"], "L": ["D"], "R": ["T"]}}

def get_puzzle_input(directory):
    with open(directory) as file:
        file = file.read().split() 

    LAYOUT = dict()
    MAX_X = len(file)   
    MAX_Y = len(file[0])

    for x, line in enumerate(file):
        for y, char in enumerate(line):
            LAYOUT[(x, y)] = char
    return LAYOUT, MAX_X, MAX_Y

def get_relative_direction(prev, current):
    x, y = current
    if prev == (x, y - 1):
        return "L"
    if prev == (x, y + 1):
        return "R"
    if prev == (x - 1, y):
        return "T"
    return "D"

def get_absolute_direction(current, direction):
    x, y = current
    if direction == "T":
        return (x - 1, y)
    if direction == "D":
        return (x + 1, y)
    if direction == "L":
        return (x, y - 1)
    return (x, y + 1)

def get_energized_tiles(prev, current):
    queue = deque()
    queue.append([prev, current])
    seen = set()

    while queue:
        prev, current = queue.popleft()
        if current not in LAYOUT or (prev, current) in seen:
            continue
        seen.add((prev, current)) 
        possible_directions = DIRECTIONS[LAYOUT[current]][get_relative_direction(prev, current)]
        for direction in possible_directions:
            queue.append([current, get_absolute_direction(current, direction)])
       
    return len(set(s[1] for s in seen))

def get_max_energized_tiles(MAX_X, MAX_Y):
    max_tiles = 0
    for y in range(MAX_Y):
        max_tiles = max(get_energized_tiles((-1, y), (0, y)), max_tiles)
        max_tiles = max(get_energized_tiles((MAX_X, y), (MAX_X - 1, y)), max_tiles)
    for x in range(MAX_X):
        max_tiles = max(get_energized_tiles((x, -1), (x, 0)), max_tiles)
        max_tiles = max(get_energized_tiles((x, MAX_Y), (x, MAX_Y - 1)), max_tiles)
    return max_tiles

LAYOUT, MAX_X, MAX_Y = get_puzzle_input(r"./puzzle_input.txt")
print(get_energized_tiles(prev=(0, -1), current=(0, 0))) 
print(get_max_energized_tiles(MAX_X, MAX_Y))