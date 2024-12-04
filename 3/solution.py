import re


def solve1(memory_region: str) -> int:
    hits = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory_region)
    return sum(int(x) * int(y) for x, y in hits)


def solve2(memory: str) -> int:
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


with open("input1.txt") as f:
    memory = f.read()

print(f"solution 1: {solve1(memory)}")  # 173529487
print(f"solution 2: {solve2(memory)}")  # 99532691
