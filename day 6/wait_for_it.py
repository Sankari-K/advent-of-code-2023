from math import sqrt

def get_puzzle_input(directory):
    document = dict()
    with open(directory) as file:  
        for line in file:
            line = line.split(":") 
            document[line[0]] = line[1].strip().split()
    return document

def modify_input(races):
    races["Time"] = ["".join(races["Time"])]
    races["Distance"] = ["".join(races["Distance"])]
    return races

def get_ways(time, distance):
    lesser = (time - sqrt(time ** 2 - 4 * distance)) // 2 + 1
    return (time + 1) - 2 * (lesser)

def get_total_ways(RACES):
    ways = 1
    number_of_races = len(RACES["Time"])
    for race in range(number_of_races):
        ways *= get_ways(int(RACES["Time"][race]), int(RACES["Distance"][race]))
    return ways

RACES = get_puzzle_input(r"./puzzle_input.txt")
print(get_total_ways(RACES))
print(get_total_ways(modify_input(RACES)))


