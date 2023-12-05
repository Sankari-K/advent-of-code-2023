def get_puzzle_input(directory):
    with open(directory) as file:   
        file = file.read().split("\n\n")
    
    seeds = get_seeds(file[0])
    mappings = get_mappings(file[1:])
    return seeds, mappings

def get_seeds(seeds):
    seeds = seeds.split(": ")[1].split(" ")
    return list(map(int, seeds))

def get_mappings(mappings):
    MAPPINGS = dict()
    for mapping in mappings:
        mapping = mapping.split("\n")
        key = mapping[0].split()[0]
        source, destination = key.split("-")[0], key.split("-")[-1]
        values = []

        for m in mapping[1:]:
            m = list(map(int, m.split()))
            values.append({destination: m[0], source: m[1], "range": m[2]})
        MAPPINGS[key] = values
    return MAPPINGS

def get_mapping(source, destination, source_number):
    req_mapping = MAPPINGS.get(f"{source}-to-{destination}", None) or MAPPINGS.get(f"{destination}-to-{source}", None)
    for req_map in req_mapping:
        if req_map[source] <= source_number < req_map[source] + req_map["range"]:
            diff = source_number - req_map[source]
            return req_map[destination] + diff
    return source_number

def get_location_number(seed):
    soil = get_mapping("seed", "soil", seed)
    fertilizer = get_mapping("soil", "fertilizer", soil)
    water = get_mapping("fertilizer", "water", fertilizer)
    light = get_mapping("water", "light", water)
    temperature = get_mapping("light", "temperature", light)
    humidity = get_mapping("temperature", "humidity", temperature)
    location = get_mapping("humidity", "location", humidity)
    return location

def get_seed_number(location):
    humidity = get_mapping("location", "humidity", location) 
    temperature = get_mapping("humidity", "temperature", humidity)
    light = get_mapping("temperature", "light", temperature)
    water = get_mapping("light", "water", light)
    fertilizer = get_mapping("water", "fertilizer", water)
    soil = get_mapping("fertilizer", "soil", fertilizer)
    seed = get_mapping("soil", "seed", soil)
    return seed

def check_seed_exists(seed_number):
    for index in range(0, len(SEEDS), 2):
        if SEEDS[index] <= seed_number < SEEDS[index] + SEEDS[index + 1]:
            return True
    return False

def get_best_seed_location():
    lowest_location = 0 # change 52390725
    while not check_seed_exists(get_seed_number(lowest_location)):
        lowest_location += 1
    return lowest_location

def get_lowest_location_number(seeds):
    return min([get_location_number(seed) for seed in seeds])

SEEDS, MAPPINGS = get_puzzle_input(r"./input.txt")
# print(get_lowest_location_number(SEEDS))
print(get_best_seed_location())