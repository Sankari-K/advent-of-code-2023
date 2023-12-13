def get_puzzle_input(directory):
    with open(directory) as file: 
        patterns = file.read().split("\n\n")
        return [pattern.split("\n") for pattern in patterns]

def get_horizontal_reflection_line(pattern, smudge_limit):
    for horizontal_line in range(1, len(pattern)):
        top, bottom = pattern[:horizontal_line][::-1], pattern[horizontal_line:]
        smudges = 0
        for top_row, bottom_row in zip(top, bottom):
            for top_char, bottom_char in zip(top_row, bottom_row):
                if top_char != bottom_char:
                    smudges += 1
        if smudges == smudge_limit:
            return horizontal_line 
    return 0

def get_summarized_notes(NOTES, smudge_limit):
    ans = 0
    for pattern in NOTES:
        ans += 100 * get_horizontal_reflection_line(pattern, smudge_limit)
        ans += get_horizontal_reflection_line(list(zip(*pattern)), smudge_limit)
    return ans

NOTES = get_puzzle_input(r"./puzzle_input.txt")
print(get_summarized_notes(NOTES, 0))
print(get_summarized_notes(NOTES, 1))