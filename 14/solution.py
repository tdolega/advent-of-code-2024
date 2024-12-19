import re

PART_1_SECONDS = 100


def calculate_safety_factor(positions: list[tuple[int, int]], width: int, height: int):
    return (
        sum(1 for x, y in positions if x < width // 2 and y < height // 2)
        * sum(1 for x, y in positions if x > width // 2 and y < height // 2)
        * sum(1 for x, y in positions if x < width // 2 and y > height // 2)
        * sum(1 for x, y in positions if x > width // 2 and y > height // 2)
    )


def solve(filename: str, width: int, height: int):
    print(filename)
    with open(filename) as f:
        robots = re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", f.read())

    positions = [(int(px), int(py)) for (px, py, _, _) in robots]
    velocities = [(int(vx), int(vy)) for (_, _, vx, vy) in robots]

    safety_factors = []
    max_seconds = max(PART_1_SECONDS, width * height)  # it will loop after this
    for _ in range(max_seconds):
        for i, ((px, py), (vx, vy)) in enumerate(zip(positions, velocities)):
            positions[i] = ((px + vx) % width, (py + vy) % height)
        safety_factors.append(calculate_safety_factor(positions, width, height))

    print(" part 1:", safety_factors[PART_1_SECONDS - 1])
    print(" part 2:", safety_factors.index(min(safety_factors)) + 1)  # it works because it happens that the tree is not centered in my input


solve("example.txt", 11, 7)  # 12
solve("input.txt", 101, 103)  # 220971520, 6355
