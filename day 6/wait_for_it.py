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

"""
time = 15
distance = 40

hold: 0     15 * 0   = distance
            14 * 1
            13 * 2
            12 * 3  (note)
            11 * 4  
            10 * 5
            9  * 6
            8  * 7
            7  * 8
            6  * 9
            5  * 10
            4  * 11   (note)
            3  * 12
            2  * 13
            1  * 14
            0  * 15

(h) * (t - h) > distance
h**2 - ht + d < 0
h**2 - 15 h + 40 = 0   (3.46, 11.53)


(time + 1) - 2 * (hold + 1)
"""





