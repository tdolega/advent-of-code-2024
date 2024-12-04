def is_safe(report: list[int]):
    diffs = [level1 - level2 for level1, level2 in zip(report, report[1:])]
    all_increasing = all(diff > 0 for diff in diffs)
    all_decreasing = all(diff < 0 for diff in diffs)
    is_gradual = all(1 <= abs(diff) <= 3 for diff in diffs)
    return (all_increasing or all_decreasing) and is_gradual


def is_safe_tolerant(report: list[int]):
    if is_safe(report):
        return True
    for i in range(len(report)):
        report_without_i = report[:i] + report[i + 1 :]
        if is_safe(report_without_i):
            return True
    return False


def solve_1(reports: list[list[int]]):
    return sum(map(is_safe, reports))


def solve_2(reports: list[list[int]]):
    return sum(map(is_safe_tolerant, reports))


with open("input.txt") as f:
    reports = [list(map(int, line.split())) for line in f]

print(f"part 1: {solve_1(reports)}")  # 624
print(f"part 2: {solve_2(reports)}")  # 658
