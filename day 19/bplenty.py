from collections import defaultdict
from functools import reduce
import copy 

def get_puzzle_input(directory):
    with open(directory) as file:
        raw_workflows = file.read().split("\n\n")[0]
    return parse_workflows(raw_workflows.split("\n"))

def parse_workflows(raw_workflows):
    WORKFLOWS = defaultdict(list)
    for raw_workflow in raw_workflows:
        name, conditions = raw_workflow.removesuffix("}").split("{")
        for condition in conditions.split(","):
            WORKFLOWS[name].append(condition.split(":"))
    return WORKFLOWS

def get_intersection(prev_set, variable, new_set):
    prev_set = copy.deepcopy(prev_set)
    prev_set[variable] = prev_set[variable].intersection(new_set)
    return prev_set

def get_set(condition, invert):
    if ">" in condition and not invert:
        variable, number = condition.split(">")
        number = int(number)
        return variable, set(range(number + 1, 4001))
    elif ">" in condition and invert:
        variable, number = condition.split(">")
        number = int(number)
        return variable, set(range(1, number + 1))
    elif "<" in condition and not invert:
        variable, number = condition.split("<")
        number = int(number)
        return variable, set(range(1, number))
    else:
        variable, number = condition.split("<")
        number = int(number)
        return variable, set(range(number, 4001))

def dfs(node, prev_ranges):
    if node == "A":
        return reduce(lambda x, y: x * y, [len(range) for range in prev_ranges.values()])
    
    ans = 0
    for conditions in WORKFLOWS[node]:
        if len(conditions) == 2:
            condition, new_node = conditions
            ans += dfs(new_node, get_intersection(prev_ranges, *get_set(condition, False)))
            prev_ranges = get_intersection(prev_ranges, *get_set(condition, True))

        if len(conditions) == 1:
           ans += dfs(conditions[0], prev_ranges)
    return ans

def get_total_ways():
    return dfs("in", {"x": set(range(1, 4001)), "m": set(range(1, 4001)), "a": set(range(1, 4001)), "s": set(range(1, 4001))})

WORKFLOWS = get_puzzle_input(r"./puzzle_input.txt")
print(get_total_ways())

