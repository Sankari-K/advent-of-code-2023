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

def do_intersect(a, b):
    a_coords, a_speed = a
    b_coords, b_speed = b

    x, y = symbols('x y')
    eq_x = Eq(a_coords[0] + x * a_speed[0] - b_coords[0] - y * b_speed[0], 0)
    eq_y = Eq(a_coords[1] + x * a_speed[1] - b_coords[1] - y * b_speed[1], 0)
    ans = solve((eq_x,eq_y), (x, y))
    
    if ans and (ans[x] >= 0 and ans[y] >= 0) and \
        (MIN_LIMIT <= a_coords[0] + ans[x] * a_speed[0] <= MAX_LIMIT) and \
        (MIN_LIMIT <= b_coords[1] + ans[y] * b_speed[1] <= MAX_LIMIT):
        return 1
    return 0

def get_total_interactions(HAILSTONES):
    return sum([do_intersect(hailstone_a, hailstone_b) for hailstone_a, hailstone_b in itertools.combinations(HAILSTONES, 2)])

HAILSTONES = get_puzzle_input(r"./puzzle_input.txt")
# MIN_LIMIT = 7
# MAX_LIMIT = 27
MIN_LIMIT = 200000000000000
MAX_LIMIT = 400000000000000
print(get_total_interactions(HAILSTONES))
