from collections import defaultdict


def correct_order(update: list[int], successors_by_predecessor: dict[int, set[int]]):
    update = update.copy()
    current_i = 0
    while current_i < len(update):
        current = update[current_i]
        predecessors = update[:current_i]
        incorrect_predecessors = successors_by_predecessor[current]
        # if there is a predecessor that should come after the current element, swap them
        for predecessor_i, predecessor in enumerate(predecessors):
            if predecessor in incorrect_predecessors:
                update[current_i], update[predecessor_i] = predecessor, current
                break
        else:
            current_i += 1
    return update


def solve(filename: str):
    print(filename)
    with open(filename) as f:
        rules, updates = f.read().split("\n\n")
    rules = [map(int, rule.split("|")) for rule in rules.splitlines()]
    updates = [list(map(int, update.split(","))) for update in updates.splitlines()]

    successors_by_predecessor = defaultdict(set)
    for before, after in rules:
        successors_by_predecessor[before].add(after)

    answer_1 = 0
    answer_2 = 0
    for original_update in updates:
        reordered_update = correct_order(original_update, successors_by_predecessor)
        median = reordered_update[len(reordered_update) // 2]
        if reordered_update == original_update:
            answer_1 += median
        else:
            answer_2 += median
    print(f" part 1: {answer_1}")
    print(f" part 2: {answer_2}")


solve("example.txt")  # 143, 123
solve("input.txt")  # 5651, 4743
