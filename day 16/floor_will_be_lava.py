from collections import deque

def get_puzzle_input(directory):
    LAYOUT = dict()
    MAX_X = MAX_Y = 0
    with open(directory) as file:
        file = file.read().split()       
        MAX_X = len(file)              
        for x, line in enumerate(file):
            MAX_Y = len(line)
            for y, char in enumerate(line):
                LAYOUT[(x, y)] = char
    return LAYOUT, MAX_X, MAX_Y

def get_energized_tiles(prev, x, y):
    queue = deque()
    queue.append([prev, x, y])
    seen = set()

    while queue:
        prev, x, y = queue.popleft()
        if (x, y) not in LAYOUT or (prev, x, y) in seen:
            continue
        seen.add((prev, x, y))

        # if previous is from the left
        if prev == (x, y - 1):
            if LAYOUT[(x, y)] in "-.":
                queue.append([(x, y), x, y + 1])
            elif LAYOUT[(x, y)] == "|":
                queue.append([(x, y), x - 1, y])
                queue.append([(x, y), x + 1, y])
            elif LAYOUT[(x, y)] == "/":
                queue.append([(x, y), x - 1, y])
            elif LAYOUT[(x, y)] == "\\":
                queue.append([(x, y), x + 1, y])
        # if previous is from the right
        elif prev == (x, y + 1):
            if LAYOUT[(x, y)] in "-.":
                queue.append([(x, y), x, y - 1])
            elif LAYOUT[(x, y)] == "|":
                queue.append([(x, y), x - 1, y])
                queue.append([(x, y), x + 1, y])
            elif LAYOUT[(x, y)] == "/":
                queue.append([(x, y), x + 1, y])
            elif LAYOUT[(x, y)] == "\\":
                queue.append([(x, y), x - 1, y])
        # if previous is from the top
        elif prev == (x - 1, y):
            if LAYOUT[(x, y)] in "|.":
                queue.append([(x, y), x + 1, y])
            elif LAYOUT[(x, y)] == "-":
                queue.append([(x, y), x, y + 1])
                queue.append([(x, y), x, y - 1])
            elif LAYOUT[(x, y)] == "/":
                queue.append([(x, y), x, y - 1])
            elif LAYOUT[(x, y)] == "\\":
                queue.append([(x, y), x, y + 1])
        # if previous is from the bottom
        elif prev == (x + 1, y):
            if LAYOUT[(x, y)] in "|.":
                queue.append([(x, y), x - 1, y])
            elif LAYOUT[(x, y)] == "-":
                queue.append([(x, y), x, y + 1])
                queue.append([(x, y), x, y - 1])
            elif LAYOUT[(x, y)] == "/":
                queue.append([(x, y), x, y + 1])
            elif LAYOUT[(x, y)] == "\\":
                queue.append([(x, y), x, y - 1])

    return len(set(s[1:] for s in seen))

def get_max_energized_tiles(MAX_X, MAX_Y):
    max_tiles = 0
    for y in range(MAX_Y):
        max_tiles = max(get_energized_tiles((-1, y), 0, y), max_tiles)
        max_tiles = max(get_energized_tiles((MAX_X, y), MAX_X - 1, y), max_tiles)
    for x in range(MAX_X):
        max_tiles = max(get_energized_tiles((x, -1), x, 0), max_tiles)
        max_tiles = max(get_energized_tiles((x, MAX_Y), x, MAX_Y - 1), max_tiles)
    return max_tiles

LAYOUT, MAX_X, MAX_Y = get_puzzle_input(r"./puzzle_input.txt")
print(get_energized_tiles((0, -1), 0, 0)) 
print(get_max_energized_tiles(MAX_X, MAX_Y))