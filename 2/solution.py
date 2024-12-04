def is_safe(report):
    diffs = [level1 - level2 for level1, level2 in zip(report, report[1:])]
    all_increasing = all(diff > 0 for diff in diffs)
    all_decreasing = all(diff < 0 for diff in diffs)
    if not all_increasing and not all_decreasing:
        return False
    is_gradual = all(1 <= abs(diff) <= 3 for diff in diffs)
    return is_gradual


def is_safe_tolerant(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        report_without_i = report[:i] + report[i + 1 :]
        if is_safe(report_without_i):
            return True
    return False


def solve_1(reports):
    return sum(map(is_safe, reports))


def solve_2(reports):
    return sum(map(is_safe_tolerant, reports))


with open("input1.txt") as f:
    reports = [list(map(int, line.split())) for line in f]

print(f"solution 1: {solve_1(reports)}")  # 624
print(f"solution 2: {solve_2(reports)}")  # 658
