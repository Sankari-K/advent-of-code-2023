import itertools, copy
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

def find_intersection(a, b, reqd_intersection=None):
    a_coords, a_speed = a
    b_coords, b_speed = b

    ta, tb = symbols('ta tb')
    eq_x = Eq(a_coords[0] + ta * a_speed[0] - b_coords[0] - tb * b_speed[0], 0)  # eqn for x coordinate
    eq_y = Eq(a_coords[1] + ta * a_speed[1] - b_coords[1] - tb * b_speed[1], 0)  # eqn for y coordinate
    ans = solve((eq_x, eq_y), (ta, tb))
    
    if len(ans) == 1 and reqd_intersection:
        tb_value = (reqd_intersection[0] - b_coords[0]) / b_speed[0]
        expr = ans[ta]
        expr = expr.subs(tb, tb_value)
        return expr == (reqd_intersection[0] - a_coords[0]) / a_speed[0]
     
    if not ans or (ans[ta] < 0) or (ans[tb] < 0):
        return False
    return a_coords[0] + ans[ta] * a_speed[0], b_coords[1] + ans[tb] * b_speed[1]


def get_total_interactions(HAILSTONES):
    interactions = 0
    for hailstone_a, hailstone_b in itertools.combinations(HAILSTONES, 2):
        intersection = find_intersection(hailstone_a, hailstone_b)
        if intersection and (MIN_LIMIT <= intersection[0] <= MAX_LIMIT) and \
        (MIN_LIMIT <= intersection[1] <= MAX_LIMIT):
            interactions += 1
    return interactions

def check_possible(velocity, HAILSTONES):
    # find the relative velocity of all the hailstones given the velocity of the rock
    # check if all the hailstones intersect at a particular point
    HAILSTONES = copy.deepcopy(HAILSTONES)
    for index, hailstone in enumerate(HAILSTONES):
        HAILSTONES[index][1] = [h - v for h, v in zip(hailstone[1], velocity)]
    # at first, check if x and y intersect sometime -> if not, exit early
    
    intersection_a = find_intersection(HAILSTONES[0], HAILSTONES[1])
    if not intersection_a:
        return tuple()
    
    for hailstone_a, hailstone_b in list(itertools.combinations(HAILSTONES, 2))[:10]:
        new_intersection = find_intersection(hailstone_a, hailstone_b, intersection_a)
        if new_intersection != intersection_a and not new_intersection:
            return tuple()
    
    for index, hailstone in enumerate(HAILSTONES):
        HAILSTONES[index][0] = hailstone[0][::-1]
        HAILSTONES[index][1] = hailstone[1][::-1]

    intersection_b = find_intersection(HAILSTONES[0], HAILSTONES[1])
    if not intersection_b:
        return tuple()
    
    for hailstone_a, hailstone_b in list(itertools.combinations(HAILSTONES, 2))[:10]:
        new_intersection = find_intersection(hailstone_a, hailstone_b, intersection_b)
        if new_intersection != intersection_b and not new_intersection:
            return tuple()
    return intersection_a + (intersection_b[0],)

def get_initial_pos():
    # generate all possible velocities and see if all hailstones intersect at a single point in the future (using relative velocity) 
    ans = check_possible((314, 19, 197), HAILSTONES)
    if ans:
        return ans

HAILSTONES = get_puzzle_input(r"./puzzle_input.txt")
# MIN_LIMIT = 7
# MAX_LIMIT = 27

MIN_LIMIT = 200000000000000
MAX_LIMIT = 400000000000000

# print(get_total_interactions(HAILSTONES))
print(sum(get_initial_pos()))
