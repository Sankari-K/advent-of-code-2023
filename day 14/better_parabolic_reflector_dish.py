from copy import deepcopy

def get_puzzle_input(directory):
    with open(directory) as file: 
        return [list(line.strip()) for line in file]

def get_load(platform):
    load = 0
    for index, line in enumerate(platform):
            load += line.count("O") * (len(line) - index)
    return load

def tilt(platform):
    for col in range(len(platform[0])):
        for row in range(len(platform)):
            if platform[row][col] == "O":
                current_index = row
                while current_index > 0 and platform[current_index - 1][col] == ".":
                    current_index -= 1
                platform[current_index][col], platform[row][col] = platform[row][col], platform[current_index][col]
    return platform 

def rotate(platform):
    return list(map(list, zip(*platform[::-1])))

def perform_cycle(platform):
    platform = tilt(platform)  # north tilt
    platform = tilt(rotate(platform)) # west tilt
    platform = (tilt(rotate(platform))) # south tilt
    platform = rotate(tilt(rotate(platform))) # east tilt
    return platform

def get_platform(platform, cycles):
    platforms = list()
    while platform not in platforms:
        platforms.append(deepcopy(platform))
        platform = perform_cycle(platform)

    indices = [i for i in range(len(platforms))]
    while indices.count(indices[-1]) != 3:
        indices.append(platforms.index(platform))
        platform = perform_cycle(platform)
    
    indices = indices[:-1]
    repeated_length = len(indices) - len(platforms)
    base_length = len(platforms) - repeated_length

    return platforms[(cycles - base_length) % repeated_length + base_length]

def get_north_support_load(platform, cycles):
    if cycles != 0:
        platform = get_platform(platform, cycles)
        return get_load(platform)
    return get_load(tilt(platform))

platform = get_puzzle_input(r"./puzzle_input.txt")
print(get_north_support_load(platform, cycles=0))
print(get_north_support_load(platform, cycles=1000000000))





