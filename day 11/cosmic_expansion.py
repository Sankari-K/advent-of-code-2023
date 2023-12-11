import itertools

def get_puzzle_input(directory):
    with open(directory) as file: 
        return [list(row.strip()) for row in file]

def get_empty_spaces(image):
    rows, cols = set(), set()

    for index, row in enumerate(image):
        if set(row) == set("."):
            rows.add(index)
            
    for index, col in enumerate([i for i in zip(*image)]):
        if set(col) == set("."):
            cols.add(index)

    return rows, cols

def get_galaxies(universe, empty_rows, empty_cols, expansion_rate):
    galaxies = []
    row_offset = 0
    for x, row in enumerate(universe):
        if x in empty_rows:
            row_offset += expansion_rate - 1
            
        col_offset = 0
        for y, point in enumerate(row):
            if y in empty_cols:
                col_offset += expansion_rate - 1
            if point == "#":
                galaxies.append([x + row_offset, y + col_offset])
    return galaxies

def get_sum_distances(GALAXIES):
    distances = 0
    for (ax, ay), (bx, by) in itertools.combinations(GALAXIES, 2):
        distances += abs(ax - bx) + abs(ay - by)
    return distances

UNIVERSE = get_puzzle_input(r"./puzzle_input.txt")
ROWS, COLS = get_empty_spaces(UNIVERSE)

GALAXIES = get_galaxies(UNIVERSE, ROWS, COLS, 2)  # part 1
GALAXIES = get_galaxies(UNIVERSE, ROWS, COLS, 1000000)  # part 2

print(get_sum_distances(GALAXIES))
