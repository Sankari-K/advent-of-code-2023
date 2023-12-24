from collections import defaultdict, deque

def get_puzzle_input(directory):
    with open(directory) as file:
        file = file.read().split("\n")
    
    BRICKS = dict()
    MAX_Z = -1

    for index, line in enumerate(file):
        start, end = line.strip().split("~")
        start = list(map(int, start.split(",")))
        end = list(map(int, end.split(",")))

        MAX_Z = max(MAX_Z, start[2])

        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                for z in range(start[2], end[2] + 1):
                    BRICKS[(x, y, z)] = index
    return BRICKS, MAX_Z

def get_bricks_given_height(z):
    return set([BRICKS[brick_pos] for brick_pos in BRICKS if brick_pos[2] == z])

def get_all_coordinates(brick_id):
    return set([brick_pos for brick_pos, brick_num in BRICKS.items() if brick_num == brick_id])
 
def simulate_gravity(BRICKS, MAX_Z):
    for level in range(1, MAX_Z + 1): # find all bricks on that level
        for brick in get_bricks_given_height(level):
            simulate_brick_fall(brick, level)
    return BRICKS
        
def simulate_brick_fall(brick, level):
    coordinates = get_all_coordinates(brick)
    xyplane = set([(coordinate[0], coordinate[1]) for coordinate in coordinates])

    lower = 1
    while all([(level - lower >= 1) and ((coordinate[0], coordinate[1], level - lower) not in BRICKS) for coordinate in xyplane]):
        lower += 1
    lower -= 1
    
    new_coordinates = [(coordinate[0], coordinate[1], coordinate[2] - lower) for coordinate in coordinates]
    for coordinate in coordinates:
        del BRICKS[coordinate]
    for coordinate in new_coordinates:
        BRICKS[coordinate] = brick

def get_support_stats(BRICKS):
    support_stats = defaultdict(set)
    for brick_id in set(BRICKS.values()):
        coordinates = get_all_coordinates(brick_id)
        xyplane = set([(coordinate[0], coordinate[1]) for coordinate in coordinates])
        max_z = max([coordinate[2] for coordinate in coordinates])

        for x, y in xyplane:
            if (x, y, max_z + 1) in BRICKS:
                support_stats[brick_id].add(BRICKS[(x, y, max_z + 1)])

    return support_stats

def get_other_fallen_bricks(brick):
    disintegrated_bricks = set([brick])
    queue = deque([brick])

    while queue:
        next_brick = queue.popleft()

        supported_bricks = []
        for brick, supports in SUPPORT_STATS.items():
            if brick not in disintegrated_bricks:
                supported_bricks.extend(supports)

        for brick in SUPPORT_STATS[next_brick]:
            if brick not in disintegrated_bricks and brick not in supported_bricks:
                disintegrated_bricks.add(brick)
                queue.append(brick)
    return len(disintegrated_bricks) - 1

def get_inconsequential_bricks(support_stats):
    inconsequential_bricks = len(set(BRICKS.values())) - len(support_stats)
    return sum([get_other_fallen_bricks(brick) == 0 for brick in list(support_stats.keys())]) + inconsequential_bricks

def get_sum_other_fallen_bricks(support_stats):
    return sum(map(get_other_fallen_bricks, list(support_stats.keys())))
   
BRICKS, MAX_Z = get_puzzle_input(r"./puzzle_input.txt")
BRICKS = simulate_gravity(BRICKS, MAX_Z)
SUPPORT_STATS = get_support_stats(BRICKS)

print(get_inconsequential_bricks(SUPPORT_STATS)) # part a
print(get_sum_other_fallen_bricks(SUPPORT_STATS)) # part b
