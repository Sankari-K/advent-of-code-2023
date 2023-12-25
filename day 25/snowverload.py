from collections import defaultdict
import networkx as nx

def get_puzzle_input(directory):
    with open(directory) as file:
        file = file.read().split("\n")
    
    WIRING = defaultdict(list)

    for line in file:
        left, right = line.split(": ")
        for component in right.split():
            WIRING[left].append(component)
            WIRING[component].append(left)
    return WIRING

def get_nx_graph(WIRING):
    nx_graph = nx.DiGraph()
    for component in WIRING:
        for child in WIRING[component]:
            nx_graph.add_edge(component, child, capacity=1)
            nx_graph.add_edge(child, component, capacity=1)
    return nx_graph, child

def get_partition(WIRING, component):
    for source_node in WIRING:
        cut_value, (parition_a, partition_b) = nx.minimum_cut(WIRING, source_node, component)
        if cut_value == 3:
            return len(parition_a) * len(partition_b)
    
WIRING = get_puzzle_input(r"./puzzle_input.txt")
WIRING, component = get_nx_graph(WIRING)
print(get_partition(WIRING, component))


