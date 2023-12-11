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
    if MAZE[(START[0] + 1, START[1])] in "|LJ":
        return get_path([START], START[0] + 1, START[1])
    return get_path([START], START[0], START[1] + 1)

def get_furthest_steps(START):
    max_path = get_loop(START)
    return len(max_path) // 2

def get_area_enclosed(START):
    path = get_loop(START)
    poly = Path(path)
    area_enclosed = 0
    for x_coordinate in range(MAX_X):
        for y_coordinate in range(MAX_Y):
                if (x_coordinate, y_coordinate) not in path:
                    if poly.contains_point((x_coordinate, y_coordinate)):
                        area_enclosed += 1
    return area_enclosed
    
MAZE, START, MAX_X, MAX_Y = get_puzzle_input(r"./puzzle_input.txt")
print(get_furthest_steps(START))
print(get_area_enclosed(START))
