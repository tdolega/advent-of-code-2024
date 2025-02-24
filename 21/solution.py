from functools import cache

NUMERIC_KEYPAD = [
    "789",
    "456",
    "123",
    " 0A",
]
ROBOTIC_KEYPAD = [
    " ^A",
    "<v>",
]


def create_graph(keypad: list[str]):
    graph = {}
    for y1, row1 in enumerate(keypad):
        for x1, cell1 in enumerate(row1):
            for y2, row2 in enumerate(keypad):
                for x2, cell2 in enumerate(row2):
                    path = "<" * (x1 - x2) + "v" * (y2 - y1) + "^" * (y1 - y2) + ">" * (x2 - x1)
                    if keypad[y1][x2] == " " or keypad[y2][x1] == " ":
                        path = path[::-1]
                    graph[(cell1, cell2)] = path + "A"
    return graph


numeric_graph = create_graph(NUMERIC_KEYPAD)
robotic_graph = create_graph(ROBOTIC_KEYPAD)


@cache
def recursive_keypress_count(source_cell: str, destination_cell: str, depth: int):
    keypresses = robotic_graph[(source_cell, destination_cell)]

    if depth == 1:
        return len(keypresses)

    aggregated_keypress_counts = 0
    for source_cell, destination_cell in zip("A" + keypresses, keypresses):
        aggregated_keypress_counts += recursive_keypress_count(source_cell, destination_cell, depth - 1)
    return aggregated_keypress_counts


def answer_for_code(code: str, n_robots: int):
    hand_sequence = ""
    for source_cell, destination_cell in zip("A" + code, code):
        hand_sequence += numeric_graph[(source_cell, destination_cell)]

    robotic_sequence_length = 0
    for source_cell, destination_cell in zip("A" + hand_sequence, hand_sequence):
        robotic_sequence_length += recursive_keypress_count(source_cell, destination_cell, n_robots)

    numeric_part_of_code = int(code[:-1])
    return robotic_sequence_length * numeric_part_of_code


def solve(filename: str):
    print(filename)
    with open(filename, "r") as f:
        codes = f.read().splitlines()

    print(" part 1:", sum(answer_for_code(code, 2) for code in codes))
    print(" part 2:", sum(answer_for_code(code, 25) for code in codes))


solve("example.txt")  # 126384
solve("input.txt")  # 162740, 203640915832208
