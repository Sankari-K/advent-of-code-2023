import re
import math

def get_puzzle_input(directory):
    with open(directory) as file: 
        file = file.read().split("\n")

    directions = file[0]
    adj_list = dict()
    for line in file[2:]:
        node, left, right = re.findall("[1-9A-Z]+", line)
        adj_list[node] = [left, right]
    return directions, adj_list

def get_frequency(node, directions, adj_list):
    steps = 0
    current_direction = 0

    while not node.endswith("Z"):
        if directions[current_direction] == "L":
            node = adj_list[node][0]
        else:
            node = adj_list[node][1]
        current_direction = (current_direction + 1) % len(directions)
        steps += 1
    return steps
        
def find_simultaneous_steps(directions, adj_list):
    frequencies = []
    for node in [node for node in adj_list if node.endswith("A")]:
        frequencies.append(get_frequency(node, directions, adj_list))
    return math.lcm(*frequencies)

directions, adj_list = get_puzzle_input(r"./puzzle_input.txt")

print(get_frequency("AAA", directions, adj_list))
print(find_simultaneous_steps(directions, adj_list))

"""
The length of ..A -> ..Z is a multiple of pattern length.

No other ..Z nodes exist between the ..Z -> ..Z path, which always has the same start and end node.

The length of ..Z -> ..Z is a multiple of pattern length.

For all pairs, ..A -> ..Z and ..Z -> ..Z are the same.
"""
