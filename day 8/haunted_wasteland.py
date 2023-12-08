from math import gcd

def get_puzzle_input(directory):
    with open(directory) as file: 
        file = file.read().split("\n")

    directions = file[0]
    adj_list = dict()
    for node in file[2:]:
        node, neighbors = node.split(" = ")
        neighbors = neighbors[1:-1].split(", ")
        adj_list[node] = neighbors
    return directions, adj_list

def get_frequency(node, directions, adj_list):
    steps = 0
    current_direction = 0
    observed_ends = []

    while len(observed_ends) != 2:
        if node[-1] == "Z":
            observed_ends.append(steps)
        if directions[current_direction] == "L":
            node = adj_list[node][0]
        else:
            node = adj_list[node][1]
        current_direction = (current_direction + 1) % len(directions)
        steps += 1
        
    return {"first occurence": observed_ends[0], "frequency": observed_ends[-1] - observed_ends[0]}

def find_simultaneous_steps(directions, adj_list):
    frequencies = []
    for node in [node for node in adj_list if node[-1] == "A"]:
        frequencies.append(get_frequency(node, directions, adj_list)["frequency"])
    return find_lcm(frequencies)

def find_lcm(array):
    lcm = 1
    for a in array:
        lcm = lcm * a // gcd(lcm, a)
    return lcm

directions, adj_list = get_puzzle_input(r"./puzzle_input.txt")

print(get_frequency("AAA", directions, adj_list)["first occurence"])
print(find_simultaneous_steps(directions, adj_list))

