from functools import lru_cache

def get_puzzle_input(directory):
    SPRINGS = []
    with open(directory) as file: 
        for line in file:
            line = line.split()
            line[1] = list(map(int, line[1].split(",")))
            SPRINGS.append(line)
    return SPRINGS

def modify_springs(springs):
    for index, spring in enumerate(springs):
        springs[index][0] = ((spring[0] + "?") * 5)[:-1]
        springs[index][1] = spring[1] * 5
    return springs

@lru_cache
def get_arrangement(spring_pos, current_pos, matched_damaged_count, current_damaged_count):
    spring, schema = SPRINGS[spring_pos]
    
    if current_pos == len(spring):
        if matched_damaged_count == len(schema):
            return 1 if current_damaged_count == 0 else 0
        elif matched_damaged_count == len(schema) - 1 and schema[matched_damaged_count] == current_damaged_count:
            return 1
        return 0
    
    if spring[current_pos] == "#":
        return get_arrangement(spring_pos, current_pos + 1, matched_damaged_count, current_damaged_count + 1)
    elif spring[current_pos] == ".":
        if current_damaged_count != 0 and matched_damaged_count >= len(schema):
            return 0
        if current_damaged_count != 0 and schema[matched_damaged_count] == current_damaged_count:
            return get_arrangement(spring_pos, current_pos + 1, matched_damaged_count + 1, 0)
        elif current_damaged_count == 0:
            return get_arrangement(spring_pos, current_pos + 1, matched_damaged_count, current_damaged_count)
        return 0
    else:
        ans = 0
        ans += get_arrangement(spring_pos, current_pos + 1, matched_damaged_count, current_damaged_count + 1)
        if current_damaged_count != 0 and matched_damaged_count < len(schema) and schema[matched_damaged_count] == current_damaged_count:
            ans += get_arrangement(spring_pos, current_pos + 1, matched_damaged_count + 1, 0)
        elif current_damaged_count == 0:
            ans += get_arrangement(spring_pos, current_pos + 1, matched_damaged_count, current_damaged_count)
        return ans

def get_sum_arrangements(SPRINGS):
    tot = 0
    for spring_pos, spring in enumerate(SPRINGS):
        tot += get_arrangement(spring_pos, 0, 0, 0)
        print(spring_pos)
    return tot
    # return sum([get_arrangement(spring_pos, 0, 0, 0) for spring_pos in range(len(SPRINGS))])

SPRINGS = get_puzzle_input(r"./puzzle_input.txt")
SPRINGS = modify_springs(SPRINGS)
print(get_sum_arrangements(SPRINGS))
