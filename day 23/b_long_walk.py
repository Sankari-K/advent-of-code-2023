from collections import defaultdict

def get_puzzle_input(directory):
    with open(directory) as file:
        file = file.read().split("\n")
    
    TRAIL = defaultdict(str)
    MAX_X, MAX_Y = len(file), len(file[0])

    for x, line in enumerate(file):
        for y, char in enumerate(line):
            TRAIL[(x, y)] = char
    return TRAIL, MAX_X, MAX_Y

def get_ends(TRAIL):
    min_x, max_x = 0, max([x for x, _ in TRAIL])
    for x, y in TRAIL:
        if x == min_x and TRAIL[(x, y)] == ".":
            min_y = y
        if x == max_x and TRAIL[(x, y)] == ".":
            max_y = y

    return (min_x, min_y), (max_x, max_y)

def get_filtered_neighbors(current_tile):
    x, y = current_tile
    neighbors = []
    for neighbor in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
        if neighbor in TRAIL and TRAIL[neighbor] != "#":
            neighbors.append(neighbor)
    return neighbors

def get_graph(TRAIL):
    ADJ_LIST = defaultdict(list)

    for x in range(MAX_X):
        for y in range(MAX_Y):
            if TRAIL[(x, y)] != "#":
                for neighbor in get_filtered_neighbors((x, y)):
                    ADJ_LIST[(x, y)].append([(neighbor[0], neighbor[1]), 1])
    return ADJ_LIST

def contract_graph(TRAIL):
    contractable_vertices = list(filter(lambda p: len(TRAIL[p]) == 2, TRAIL))
    while contractable_vertices:
        for vertex in contractable_vertices:
            (neighbor_a, edge_a), (neighbor_b, edge_b) = TRAIL[vertex]
            TRAIL[neighbor_a].remove([vertex, edge_a])
            TRAIL[neighbor_b].remove([vertex, edge_b])

            TRAIL[neighbor_a].append([neighbor_b, edge_a + edge_b])
            TRAIL[neighbor_b].append([neighbor_a, edge_a + edge_b])
            del TRAIL[vertex]
        contractable_vertices = list(filter(lambda p: len(TRAIL[p]) == 2, TRAIL))
    
    return TRAIL

def get_longest_hike(current, path, distance_travelled):
    global MAX_STEPS

    if current == END:
        MAX_STEPS = max(MAX_STEPS, distance_travelled)
        return

    for neighbor, distance in TRAIL[current]:
        if neighbor not in path:
            path.add(neighbor)
            get_longest_hike(neighbor, path, distance_travelled + distance) 
            path.remove(neighbor)

TRAIL, MAX_X, MAX_Y = get_puzzle_input(r"./puzzle_input.txt")
START, END = get_ends(TRAIL)
TRAIL = contract_graph(get_graph(TRAIL))

MAX_STEPS = -1
get_longest_hike(START, set(), 0)
print(MAX_STEPS)
