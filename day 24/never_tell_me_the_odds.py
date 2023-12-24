import itertools
from sympy import symbols, Eq, solve

def get_puzzle_input(directory):
    with open(directory) as file:
        file = file.read().split("\n")

    HAILSTONES = list()
    for hailstone in file:
        current_pos, speed = hailstone.split(" @ ")
        current_pos = list(map(int, current_pos.split(", ")))
        speed = list(map(int, speed.split(", ")))
        HAILSTONES.append([current_pos, speed])
    return HAILSTONES

def find_intersection(a, b):
    a_coords, a_speed = a
    b_coords, b_speed = b

    x, y = symbols('x y')
    eq_x = Eq(a_coords[0] + x * a_speed[0] - b_coords[0] - y * b_speed[0], 0)
    eq_y = Eq(a_coords[1] + x * a_speed[1] - b_coords[1] - y * b_speed[1], 0)
    ans = solve((eq_x,eq_y), (x, y))

    if not ans or (ans[x] < 0) or (ans[y] < 0):
        return False
    return a_coords[0] + ans[x] * a_speed[0], b_coords[1] + ans[y] * b_speed[1]


def get_total_interactions(HAILSTONES):
    interactions = 0
    for hailstone_a, hailstone_b in itertools.combinations(HAILSTONES, 2):
        intersection = find_intersection(hailstone_a, hailstone_b)
        if intersection and (MIN_LIMIT <= intersection[0] <= MAX_LIMIT) and \
        (MIN_LIMIT <= intersection[1] <= MAX_LIMIT):
            interactions += 1
    return interactions

HAILSTONES = get_puzzle_input(r"./puzzle_input.txt")
# MIN_LIMIT = 7
# MAX_LIMIT = 27
MIN_LIMIT = 200000000000000
MAX_LIMIT = 400000000000000
print(get_total_interactions(HAILSTONES))
