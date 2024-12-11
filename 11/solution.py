from functools import cache


def apply_rule(stone: int):
    if stone == 0:
        return (1,)

    s = str(stone)
    if len(s) % 2 == 0:
        h = len(s) // 2
        return (int(s[h:]), int(s[:h]))

    return (stone * 2024,)


@cache
def calculate_length(stone: int, n_blinks: int):
    if n_blinks == 0:
        return 1
    return sum(calculate_length(stone, n_blinks - 1) for stone in apply_rule(stone))


def solve(filename: str):
    print(filename)
    with open(filename) as f:
        stones = tuple(map(int, f.read().split()))

    print(" part 1:", sum(calculate_length(stone, 25) for stone in stones))
    print(" part 2:", sum(calculate_length(stone, 75) for stone in stones))


solve("example.txt")  # 55312
solve("input.txt")  # 200446, 238317474993392
