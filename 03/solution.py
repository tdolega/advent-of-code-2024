import re


def solve1(memory_region: str):
    hits = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory_region)
    return sum(int(x) * int(y) for x, y in hits)


def solve2(memory: str):
    ENABLE_PATTERN = "do()"
    DISABLE_PATTERN = "don't()"
    solution = 0
    start = 0
    end = 0
    while start != -1 and end < len(memory):
        end = memory.find(DISABLE_PATTERN, start)
        if end == -1:
            end = len(memory)
        solution += solve1(memory[start:end])
        start = memory.find(ENABLE_PATTERN, end)
    return solution


def solve(filename: str):
    print(filename)
    with open(filename) as f:
        memory = f.read()

    print(f" part 1: {solve1(memory)}")
    print(f" part 2: {solve2(memory)}")


solve("example.txt")  # 161, 48
solve("input.txt")  # 173529487, 99532691
