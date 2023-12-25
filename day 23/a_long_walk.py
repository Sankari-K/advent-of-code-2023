import heapq
from collections import defaultdict, deque

DIRECTIONS = {">": lambda x, y: (x, y + 1),
              "<": lambda x, y: (x, y - 1),
              "v": lambda x, y: (x + 1, y),
              "^": lambda x, y: (x - 1, y)}

def get_puzzle_input(directory):
    with open(directory) as file:
        file = file.read().split()
    
    TRAIL = defaultdict(str)

    for x, line in enumerate(file):
        for y, char in enumerate(line):
            TRAIL[(x, y)] = char
    return TRAIL

def get_ends(TRAIL):
    min_x, max_x = 0, max([x for x, _ in TRAIL])
    for x, y in TRAIL:
        if x == min_x and TRAIL[(x, y)] == ".":
            min_y = y
        if x == max_x and TRAIL[(x, y)] == ".":
            max_y = y

    return (min_x, min_y), (max_x, max_y)

def get_longest_hike(START, END):
    MAX_STEPS = -1
    queue = [[0, START, set()]]  # distance_travelled, current_pos, prev, set of all seen tiles 

    while queue:
        distance_travelled, current_tile, seen_tiles = heapq.heappop(queue)
        
        if current_tile == END:
            MAX_STEPS = max(MAX_STEPS, -1 * distance_travelled)
            continue
        
        if TRAIL[current_tile] in DIRECTIONS:
            next = DIRECTIONS[TRAIL[current_tile]](*current_tile)
            if TRAIL[next] != "#" and next in TRAIL and next not in seen_tiles: 
                heapq.heappush(queue, [-1 * (-1 * distance_travelled + 1), next, seen_tiles.union(set([current_tile]))])
            continue

        # assuming it is a "." tile
        for neighbor in get_filtered_neighbors(current_tile):
            if neighbor not in seen_tiles:
                heapq.heappush(queue, [-1 * (-1 * distance_travelled + 1), neighbor, seen_tiles.union(set([current_tile]))])
    return MAX_STEPS

def get_filtered_neighbors(current_tile):
    x, y = current_tile
    neighbors = []
    for neighbor in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
        if neighbor in TRAIL and TRAIL[neighbor] != "#":
            neighbors.append(neighbor)
    return neighbors

TRAIL = get_puzzle_input(r"./puzzle_input.txt")
START, END = get_ends(TRAIL)
print(get_longest_hike(START, END))  # part a

