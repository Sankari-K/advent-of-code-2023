from collections import OrderedDict, defaultdict

def get_puzzle_input(directory):
    with open(directory) as file: 
        return file.read().split(",")

def hash(step):
    current = 0
    for char in step:
        current = ((current + ord(char)) * 17) % 256
    return current

def sum_hashes(intialization_sequence):
    return sum(map(hash, intialization_sequence))

def hashmap(initialization_sequence):
    boxes = defaultdict(OrderedDict)
    for step in initialization_sequence:
        if "=" in step:
            label, focal_length = step.split("=")
            box = hash(label)
            boxes[box][label] = focal_length
        if "-" in step:
            label, focal_length = step.split("-")
            box = hash(label)
            if label in boxes[box]:
                del boxes[box][label]
    
    total_focusing_power = 0
    for box_number, lenses in boxes.items():
        for slot, focal_length in enumerate(lenses.values(), start=1):
            total_focusing_power += (box_number + 1) * slot * int(focal_length)
    return total_focusing_power

intialization_sequence = get_puzzle_input(r"./puzzle_input.txt")
print(sum_hashes(intialization_sequence))
print(hashmap(intialization_sequence))