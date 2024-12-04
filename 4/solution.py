import re
from collections import defaultdict


def find_line(line: str, needle: str):
    return [(m.start() + m.end()) // 2 for m in re.finditer(needle, line)]


def find_horizontal(lines: list[str], needle: str):
    return [(x, y) for y, line in enumerate(lines) for x in find_line(line, needle)]


def find_vertical(lines: list[str], needle: str):
    hits = find_horizontal(["".join(line) for line in zip(*lines)], needle)
    return [(y, x) for x, y in hits]


def find_diagonal(lines: list[str], needle: str):
    f_points = defaultdict(list)
    b_points = defaultdict(list)
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            point = (i, j, line[j])
            f_points[i + j].append(point)
            b_points[i - j].append(point)

    # find needle, then transform from diagonal coordinates to regular coordinates, to properly match forward and backward points
    def find_and_transform(points: dict[int, list[tuple[int, int, str]]]):
        points = list(points.values())
        chars = ["".join([point[2] for point in points]) for points in points]
        hits = find_horizontal(chars, needle)
        return [points[y][x][:2] for x, y in hits]

    return find_and_transform(f_points), find_and_transform(b_points)


def find_dir(lines: list[str], needle: str):
    fdiag, bdiag = find_diagonal(lines, needle)
    return find_horizontal(lines, needle) + find_vertical(lines, needle) + fdiag + bdiag


def find_bidir(lines: list[str], needle: str):
    return find_dir(lines, needle) + find_dir(lines, needle[::-1])


def find_x(lines: list[str], needle: str):
    fdiag_std, bdiag_std = find_diagonal(lines, needle)
    fdiag_rev, bdiag_rev = find_diagonal(lines, needle[::-1])
    fdiag = set(fdiag_std + fdiag_rev)
    bdiag = set(bdiag_std + bdiag_rev)
    return fdiag & bdiag


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

print(f"part 1: {len(find_bidir(lines, "XMAS"))}")  # 2414
print(f"part 2: {len(find_x(lines, "MAS"))}")  # 1871
