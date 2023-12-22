def get_puzzle_input(directory):
    with open(directory) as file:
        file = file.read().split("\n")
    
    BRICKS = dict()
    MAX_DIMENSIONS = [-1, -1, -1]
    for index, line in enumerate(file):
        old, new = line.strip().split("~")
        old = list(map(int, old.split(",")))
        new = list(map(int, new.split(",")))
        for x in range(old[0], new[0] + 1):
            for y in range(old[1], new[1] + 1):
                for z in range(old[2], new[2] + 1):
                    BRICKS[(x, y, z)] = index
                    MAX_DIMENSIONS = [max(MAX_DIMENSIONS[0], x), max(MAX_DIMENSIONS[1], y), max(MAX_DIMENSIONS[2], z)]
    return BRICKS, MAX_DIMENSIONS

def get_bricks_given_height(z):
    req_bricks = set()
    for brick in BRICKS:
        if brick[2] == z:
            req_bricks.add(BRICKS[brick])
    return req_bricks

def get_all_coordinates(brick_id):
    coordinates = set()
    for brick_pos, brick_num in BRICKS.items():
        if brick_num == brick_id:
            coordinates.add(brick_pos)
    return coordinates

def simulate_entire_fall(BRICKS, MAX_Z):
    for level in range(1, MAX_Z + 1):
        # find all brick types in that level
        all_bricks = get_bricks_given_height(level)
        for brick in all_bricks:
            simulate_fall_brick(brick, level)
    return BRICKS
        
def simulate_fall_brick(brick, level):
    coordinates = get_all_coordinates(brick)
    xyplane = set([(coordinate[0], coordinate[1]) for coordinate in coordinates])

    lower = 1
    while all([((coordinate[0], coordinate[1], level - lower) not in BRICKS) and (level - lower >= 1) for coordinate in xyplane]):
        lower += 1
    lower -= 1

    for coordinate in coordinates:
        del BRICKS[coordinate]
        BRICKS[(coordinate[0], coordinate[1], coordinate[2] - lower)] = brick

def get_support_stats(BRICKS):
    for brick_id in set(BRICKS.values()):
        print(brick_id)

BRICKS, MAX_DIMENSIONS = get_puzzle_input(r"./input.txt")
BRICKS = simulate_entire_fall(BRICKS, MAX_DIMENSIONS[-1])
get_support_stats(BRICKS)
