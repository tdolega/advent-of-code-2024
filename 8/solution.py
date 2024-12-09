def find_antinodes(antennas: list[list[(int, int)]], w: int, h: int, multiple_harmonics: bool):
    antinodes = set()
    for locations in antennas:
        for location_idx, (x1, y1) in enumerate(locations):
            other_locations = locations[:location_idx] + locations[location_idx + 1 :]
            for x2, y2 in other_locations:
                dx = x1 - x2
                dy = y1 - y2
                harmonic = 0 if multiple_harmonics else 1
                while True:
                    x3 = x1 + dx * harmonic
                    y3 = y1 + dy * harmonic
                    if x3 < 0 or x3 >= w or y3 < 0 or y3 >= h:
                        break
                    antinodes.add((x3, y3))
                    if not multiple_harmonics:
                        break
                    harmonic += 1
    return antinodes


def solve(filename: str):
    print(filename)
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    w, h = len(lines[0]), len(lines)

    antennas = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ".":
                continue
            antennas.setdefault(c, []).append((x, y))
    antennas = antennas.values()

    print(" part 1:", len(find_antinodes(antennas, w, h, multiple_harmonics=False)))
    print(" part 2:", len(find_antinodes(antennas, w, h, multiple_harmonics=True)))


solve("example.txt")  # 14, 34
solve("input.txt")  # 379, 1339
