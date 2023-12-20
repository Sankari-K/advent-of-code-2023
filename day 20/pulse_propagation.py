from collections import deque
import math 

QUEUE = deque()

class Broadcast:
    def __init__(self, destination):
        self.destination = destination
    
    def receive_pulse(self, source, pulse_type):
        for module in self.destination:
            self.send_pulse(module, pulse_type)
        
    def send_pulse(self, destination, pulse_type):
        QUEUE.append(("broadcaster", pulse_type, destination))

class FlipFlop:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination
        self.current_status = False
    
    def refresh(self):
        self.current_status = False

    def receive_pulse(self, source, pulse_type):
        if pulse_type == "low":
            if self.current_status == False:
                self.current_status = True
                for module in self.destination:
                    self.send_pulse(module, "high")
            else:
                self.current_status = False
                for module in self.destination:
                    self.send_pulse(module, "low")

    def send_pulse(self, destination, pulse_type):
        QUEUE.append((self.name, pulse_type, destination))

class Conjunction:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination
    
    def refresh(self):
        self.current_status = {s: "low" for s in self.current_status}

    def set_inputs(self, inputs):
        self.current_status = {d: "low" for d in inputs}

    def receive_pulse(self, source, pulse_type):
        self.current_status[source] = pulse_type

        if all([current == "high" for current in self.current_status.values()]):
            for module in self.destination:
                self.send_pulse(module, "low")
        else:
            for module in self.destination:
                self.send_pulse(module, "high")

    def send_pulse(self, destination, pulse_type):
        QUEUE.append((self.name, pulse_type, destination))


def get_puzzle_input(directory):
    with open(directory) as file:
        file = file.read().split("\n")
    
    MODULES = dict()
    for line in file:
        source, destination = line.split(" -> ")
        destination = destination.split(", ")
        
        if source == "broadcaster":
            MODULES[source] = Broadcast(destination)
            continue
        source_name = source[1:]
        if source[0] == "%":
            MODULES[source_name] = FlipFlop(source_name, destination)
        elif source[0] == "&":
            MODULES[source_name] = Conjunction(source_name, destination)
    
    for module in MODULES:
        if isinstance(MODULES[module], Conjunction):
            inputs = []
            for others in MODULES:
                if module in MODULES[others].destination:
                    inputs.append(others)
            MODULES[module].set_inputs(inputs)
    return MODULES

def push_button(times):
    pushes = {"low": 0, "high": 0}
    for _ in range(times):
        pushes["low"] += 1
        MODULES["broadcaster"].receive_pulse(None, "low")
        while QUEUE:
            sender, pulse, receiver = QUEUE.popleft()
            pushes[pulse] += 1
            if receiver not in MODULES:
                continue
            MODULES[receiver].receive_pulse(sender, pulse)
    return pushes["low"] * pushes["high"]
        
def switch_on_rz(module, node):
    for component in MODULES:
        if isinstance(MODULES[component], FlipFlop) or isinstance(MODULES[component], Conjunction):
            MODULES[component].refresh()

    button_presses = 1
    while True:
        MODULES["broadcaster"].receive_pulse(None, "low")
        while QUEUE:
            sender, pulse, receiver = QUEUE.popleft()
            
            if MODULES[module].current_status[node] == "high":
                return button_presses
            
            if receiver in MODULES:
                MODULES[receiver].receive_pulse(sender, pulse)
        button_presses += 1

def get_frequency(module):
    lcm = []
    for nodes in MODULES[module].current_status:
        lcm.append(switch_on_rz(module, nodes))
    return math.lcm(*lcm)
    

MODULES = get_puzzle_input(r"./puzzle_input.txt")
print(push_button(1000))
print(get_frequency("hf"))

    


