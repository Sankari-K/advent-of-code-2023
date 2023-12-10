def get_puzzle_input(directory):
    MAZE = dict()
    START = tuple()
    with open(directory) as file: 
        file = file.read().split("\n")
        MAX_X = len(file)
        MAX_Y = len(file[0])
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
        # if we're coming from the left: can move only if "-", "J", "7"
        if previous == (x, y - 1):
            if MAZE[(x, y)] == "-":
                (x, y) = (x, y + 1)
            elif MAZE[(x, y)] == "J":
                (x, y) = (x - 1, y)
            elif MAZE[(x, y)] == "7":
                (x, y) = (x + 1, y)
        # if we're coming from the right: can move only if "-", "L", "F"
        elif previous == (x, y + 1):
            if MAZE[(x, y)] == "-":
                (x, y) = (x, y - 1)
            elif MAZE[(x, y)] == "L":
                (x, y) = (x - 1, y)
            elif MAZE[(x, y)] == "F":
                (x, y) = (x + 1, y)
        # if we're coming from the top: can move only if "|", "L", "J"
        elif previous == (x - 1, y):
            if MAZE[(x, y)] == "|":
                (x, y) =  (x + 1, y)
            elif MAZE[(x, y)] == "L":
                (x, y) = (x, y + 1)
            elif MAZE[(x, y)] == "J":
                (x, y) = (x, y - 1)
        # if we're coming from the bottom: can move only if "|", "7", "F"
        else:
            if MAZE[(x, y)] == "|":
                (x, y) = (x - 1, y)
            elif MAZE[(x, y)] == "7":
                (x, y) = (x, y - 1)
            elif MAZE[(x, y)] == "F":
                (x, y) = (x, y + 1)
    return path

def get_loop(START):
    if MAZE[(START[0] + 1, START[1])] in "|LJ":
        return get_path([START], START[0] + 1, START[1])
    return get_path([START], START[0], START[1] + 1)

def get_furthest_steps(START):
    max_path = get_loop(START)
    return len(max_path) // 2

def get_area_enclosed(START):
    path = get_loop(START)
    area_enclosed = 0
    for x_coordinate in range(MAX_X):
        is_outside = True
        prev = ""
        for y_coordinate in range(MAX_Y):
            if (x_coordinate, y_coordinate) in path:
                if MAZE[(x_coordinate, y_coordinate)] == "|":
                    is_outside = not is_outside
                elif MAZE[(x_coordinate, y_coordinate)] == "J" and prev == "F":
                    is_outside = not is_outside
                elif MAZE[(x_coordinate, y_coordinate)] == "7" and prev == "L":
                    is_outside = not is_outside
                
                if MAZE[(x_coordinate, y_coordinate)] != "-":
                    prev = MAZE[(x_coordinate, y_coordinate)]
            else:
                if not is_outside:
                    area_enclosed += 1
    return area_enclosed
    
MAZE, START, MAX_X, MAX_Y = get_puzzle_input(r"./puzzle_input.txt")
# print(get_furthest_steps(START))
print(get_area_enclosed(START))
