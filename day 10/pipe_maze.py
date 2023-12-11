from matplotlib.path import Path

def get_puzzle_input(directory):
    MAZE = dict()
    with open(directory) as file: 
        file = file.read().split("\n")
        MAX_X, MAX_Y = len(file), len(file[0])
        for x_coordinate, line in enumerate(file):
            for y_coordinate, pipe in enumerate(line.strip()):
                MAZE[(x_coordinate, y_coordinate)] = pipe
                if pipe == "S":
                    START = (x_coordinate, y_coordinate)
    return MAZE, START, MAX_X, MAX_Y

def get_path(path, x, y):
    while path and (x, y) != START:
        previous = path[-1]
        path.append((x, y))
        (x, y) = get_next_pipe(x, y, previous)
    return path

def get_next_pipe(x, y, previous):
    # if we're coming from the left: can move only if "-", "J", "7"
    if previous == (x, y - 1):
        if MAZE[(x, y)] == "-":
            return (x, y + 1)
        elif MAZE[(x, y)] == "J":
            return (x - 1, y)
        elif MAZE[(x, y)] == "7":
            return (x + 1, y)
    # if we're coming from the right: can move only if "-", "L", "F"
    elif previous == (x, y + 1):
        if MAZE[(x, y)] == "-":
            return (x, y - 1)
        elif MAZE[(x, y)] == "L":
            return (x - 1, y)
        elif MAZE[(x, y)] == "F":
            return (x + 1, y)
    # if we're coming from the top: can move only if "|", "L", "J"
    elif previous == (x - 1, y):
        if MAZE[(x, y)] == "|":
            return (x + 1, y)
        elif MAZE[(x, y)] == "L":
            return (x, y + 1)
        elif MAZE[(x, y)] == "J":
            return (x, y - 1)
    # if we're coming from the bottom: can move only if "|", "7", "F"
    else:
        if MAZE[(x, y)] == "|":
            return (x - 1, y)
        elif MAZE[(x, y)] == "7":
            return (x, y - 1)
        elif MAZE[(x, y)] == "F":
            return (x, y + 1)

def get_loop(START):   
    # check if the adj cell is part of the grid (in case S in the edges/corners of the grid)
    if (START[0] + 1, START[1]) in MAZE and MAZE[(START[0] + 1, START[1])] in "|LJ":
        return get_path([START], START[0] + 1, START[1]) # down
    elif (START[0] + 1, START[1]) in MAZE and MAZE[(START[0] + 1, START[1])] in "7-J":
        return get_path([START], START[0], START[1] + 1) # right
    return get_path([START], START[0] - 1, START[1]) # up

def get_furthest_steps(START):
    max_path = get_loop(START)
    return len(max_path) // 2

# Three ways to solve this: (a) inbuilt library in python (treat path as polygon)
#                           (b) shoelace theorem and pick's formula
#                           (c) scanline, decipher whether we're on the outside/inside via the "vertical walls" we jump through

# def get_tiles_enclosed(START):
#     path = get_loop(START)
#     poly = Path(path)
#     tiles_enclosed = 0
#     for x_coordinate in range(MAX_X):
#         for y_coordinate in range(MAX_Y):
#                 if (x_coordinate, y_coordinate) not in path:
#                     if poly.contains_point((x_coordinate, y_coordinate)):
#                         tiles_enclosed += 1
#     return tiles_enclosed

# def get_tiles_enclosed(START):
#     path = list(get_loop(START))
#     area = 0
#     path = [path[-1]] + path + [path[0]]
#     for i, point in enumerate(path[1:-1], start=1):
#         area += point[1] * (path[i - 1][0] - path[i + 1][0])
#     area = 0.5 * abs(area)
#     return int((2 * (area + 1) - (len(path) - 2)) // 2)

def get_tiles_enclosed(START):
    # replace the S by the correct pipe
    MAZE[START] = "|"   # hardcoding ftw (?)

    tiles_enclosed = 0
    path = get_loop(START)
    for x in range(MAX_X):
        prev = ""
        is_outside = True
        for y in range(MAX_Y):
            if (x, y) in path:
                if MAZE[(x, y)] == "|":
                    is_outside = not is_outside
                if MAZE[(x, y)] == "J" and prev == "F" or MAZE[(x, y)] == "7" and prev == "L":
                    is_outside = not is_outside
                if MAZE[(x, y)] != "-":
                    prev = MAZE[(x, y)]
            elif not is_outside:
                tiles_enclosed += 1
    return tiles_enclosed


MAZE, START, MAX_X, MAX_Y = get_puzzle_input(r"puzzle_input.txt")
print(get_furthest_steps(START))
print(get_tiles_enclosed(START))
