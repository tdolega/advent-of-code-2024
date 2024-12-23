from functools import cache


@cache
def count_possible(patterns: tuple[str], design: str):
    answer = 0
    for pattern in patterns:
        if design.startswith(pattern):
            rest = design[len(pattern) :]
            answer += count_possible(patterns, rest) if rest else 1
    return answer


def solve(filename: str):
    print(filename)
    with open(filename) as f:
        patterns, designs = f.read().strip().split("\n\n")
        patterns = tuple(patterns.split(", "))
        designs = designs.split("\n")

    combinations = [count_possible(patterns, design) for design in designs]
    print(" part 1:", sum(combination > 0 for combination in combinations))
    print(" part 2:", sum(combinations))


solve("example.txt")  # 6, 16
solve("input.txt")  # 327, 772696486795255
