from collections import defaultdict, deque

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
    return set([BRICKS[brick] for brick in BRICKS if brick[2] == z])

def get_all_coordinates(brick_id):
    coordinates = set()
    for brick_pos, brick_num in BRICKS.items():
        if brick_id == brick_num:
            coordinates.add(brick_pos)
    return coordinates

def simulate_entire_fall(BRICKS, MAX_Z):
    for level in range(1, MAX_Z + 1): # find all brick types on that level
        for brick in get_bricks_given_height(level):
            simulate_fall_brick(brick, level)
    return BRICKS
        
def simulate_fall_brick(brick, level):
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

def get_safe_bricks(support_stats):
    can_be_disintegrated = 0
    for brick_id, supporting_bricks in support_stats.items():
       other_values = set([s for brick, supports in support_stats.items() for s in supports  if brick != brick_id])
       if len(supporting_bricks) - len(other_values.intersection(set(supporting_bricks))) == 0:
           can_be_disintegrated += 1
    
    return can_be_disintegrated + len(set(BRICKS.values())) - len(support_stats)

def get_brick_score(brick):
    seen = set([brick])
    queue = deque([brick])

    while queue:
        next_brick = queue.popleft()

        other_values = []
        for brick, supports in SUPPORT_STATS.items():
            if brick not in seen:
                other_values.extend(supports)

        for support_brick in SUPPORT_STATS[next_brick]:
            if support_brick not in seen and support_brick not in other_values:
                seen.add(support_brick)
                queue.append(support_brick)
    return len(seen) - 1

def get_sum_fallen_bricks(support_stats):
    ans = 0
    for brick_id in list(support_stats.keys()):
        ans += get_brick_score(brick_id)
    return ans

BRICKS, MAX_DIMENSIONS = get_puzzle_input(r"./puzzle_input.txt")
BRICKS = simulate_entire_fall(BRICKS, MAX_DIMENSIONS[-1])
SUPPORT_STATS = get_support_stats(BRICKS)

print(get_safe_bricks(SUPPORT_STATS))
print(get_sum_fallen_bricks(SUPPORT_STATS))
