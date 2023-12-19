from collections import defaultdict

def get_puzzle_input(directory):
    with open(directory) as file:
        raw_workflows, raw_parts = file.read().split("\n\n")
    WORKFLOWS = parse_workflows(raw_workflows.split("\n"))
    PARTS = parse_parts(raw_parts.split("\n"))
    return WORKFLOWS, PARTS

def parse_parts(raw_parts):
    PARTS = list()
    for raw_part in raw_parts:
        part = dict()
        raw_part = raw_part[1:-1].split(",")
        for category in raw_part:
            category, amount = category.split("=")
            part[category] = int(amount)
        PARTS.append(part)
    return PARTS

def parse_workflows(raw_workflows):
    WORKFLOWS = defaultdict(list)
    for raw_workflow in raw_workflows:
        name, conditions = raw_workflow.removesuffix("}").split("{")
        for condition in conditions.split(","):
            WORKFLOWS[name].append(condition.split(":"))
    return WORKFLOWS

def check_condition(condition, part):
    categories = ["x", "m", "a", "s"]
    for category in categories:
        condition = condition.replace(category, str(part[category]))
    return eval(condition)

def process_workflow(part, WORKFLOW):
    for condition in WORKFLOW:
        if len(condition) == 1:
            return condition[0]
        if check_condition(condition[0], part):
            return condition[1]
        
def get_end_state(part, WORKFLOWS):
    next_workflow = "in"
    while next_workflow not in ["A", "R"]:
        next_workflow = process_workflow(part, WORKFLOWS[next_workflow])
    return next_workflow

def get_total_accepted_ratings(WORKFLOWS, PARTS):
    total = 0
    for part in PARTS:
        if get_end_state(part, WORKFLOWS) == "A":
            total += sum(part.values())
    return total

WORKFLOWS, PARTS = get_puzzle_input(r"./puzzle_input.txt")
print(get_total_accepted_ratings(WORKFLOWS, PARTS))