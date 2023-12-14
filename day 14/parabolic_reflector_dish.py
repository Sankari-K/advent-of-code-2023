def get_puzzle_input(directory):
    with open(directory) as file: 
        return [line.strip() for line in file]

def get_load(platform):
    load = 0
    for index, line in enumerate(platform):
        for char in line:
            if char == "O":
                load += len(line) - index
    return load

def tilt_row(line):
    line = list(line)
    for index, char in enumerate(line):
        if char == "O":
            current_index = index
            while current_index > 0 and line[current_index - 1] == ".":
                current_index -= 1
            line[current_index], line[index] = line[index], line[current_index]
    return line

def tilt_platform(platform, direction):
    if direction == "north":
        platform = list(zip(*platform))
    elif direction == "south":
        platform = list(zip(*platform[::-1]))
    elif direction == "east":
        platform = [i[::-1] for i in platform]

    for index, row in enumerate(platform):
        platform[index] = tilt_row(row)

    if direction == "north":
        platform = list(zip(*platform))
    elif direction == "south":
        platform = list(zip(*platform))[::-1]
    elif direction == "east":
        platform = [i[::-1] for i in platform]
    return platform
        
def find_pattern(platform, cycle):
    platforms = list()
    while platform not in platforms:
        platforms.append(platform)
        platform = tilt_platform(platform, "north") # north
        platform = tilt_platform(platform, "west") # west
        platform = tilt_platform(platform, "south") # south
        platform = tilt_platform(platform, "east") # east
        
    indices = [i for i in range(len(platforms))]
    while indices.count(indices[-1]) != 3:
        indices.append(platforms.index(platform))
        platform = tilt_platform(platform, "north") # north
        platform = tilt_platform(platform, "west") # west
        platform = tilt_platform(platform, "south") # south
        platform = tilt_platform(platform, "east") # east

    indices = indices[:-1]
    repeated_length = len(indices) - len(platforms)
    base_length = len(platforms) - repeated_length

    return platforms[(cycle - base_length) % repeated_length + base_length]

def get_north_load(platform):
    return get_load(tilt_platform(platform, "north"))

platform = get_puzzle_input(r"./puzzle_input.txt")
# print(get_north_load(platform)) # part a

print(get_load(find_pattern(platform, 1000000000)))

