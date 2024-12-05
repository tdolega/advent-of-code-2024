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


def solve(filename: str):
    print(filename)
    with open(filename) as f:
        reports = [list(map(int, line.split())) for line in f]

    answer_1 = sum(map(is_safe, reports))
    answer_2 = sum(map(is_safe_tolerant, reports))

    print(f" part 1: {answer_1}")
    print(f" part 2: {answer_2}")


solve("example.txt")  # 2, 4
solve("input.txt")  # 624, 658
