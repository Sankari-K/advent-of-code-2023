def get_puzzle_input(directory):
    with open(directory) as file: 
        patterns = file.read().split("\n\n")
        return [pattern.split("\n") for pattern in patterns]

def get_horizontal_reflection_line(pattern, smudges_exist):
    for horizontal_line in range(1, len(pattern)):
        top, bottom = pattern[:horizontal_line], pattern[horizontal_line:]
        min_length = min(len(top), len(bottom))
        top, bottom = top[-1 * min_length:], bottom[:min_length][::-1]

        if smudges_exist:
            smudges = 0
            for top_row, bottom_row in zip(top, bottom):
                for top_char, bottom_char in zip(top_row, bottom_row):
                    if top_char != bottom_char:
                        smudges += 1
            if smudges == 1:
                return horizontal_line 
        elif top == bottom:
            return horizontal_line
    return 0

def get_summarized_notes(NOTES, smudges_exist=False):
    ans = 0
    for pattern in NOTES:
        ans += 100 * get_horizontal_reflection_line(pattern, smudges_exist)
        ans += get_horizontal_reflection_line(list(zip(*pattern)), smudges_exist)
    return ans

NOTES = get_puzzle_input(r"./puzzle_input.txt")
print(get_summarized_notes(NOTES))
print(get_summarized_notes(NOTES, True))