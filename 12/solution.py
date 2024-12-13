def find_fences(garden: list[list[str]], visited: set[tuple[int, int]], plant: str, last_x: int, last_y: int, dx: int, dy: int):
    x, y = last_x + dx, last_y + dy
    if (x, y) in visited:
        return []
    if y < 0 or y >= len(garden) or x < 0 or x >= len(garden[y]) or garden[y][x] != plant:
        return [(last_x, last_y, dx, dy)]  # fence location and direction
    visited.add((x, y))
    return sum((find_fences(garden, visited, plant, x, y, dx, dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]), start=[])


def solve(filename: str):
    print(filename)
    with open(filename) as f:
        garden = list(map(list, f.read().splitlines()))
    h, w = len(garden), len(garden[0])

    answer_1 = 0
    answer_2 = 0
    visited_cords = set()
    for y, line in enumerate(garden):
        for x, plant in enumerate(line):
            if (x, y) in visited_cords:
                continue

            plant = garden[y][x]
            plant_cords = set()
            fences = find_fences(garden, plant_cords, plant, x, y, 0, 0)
            visited_cords.update(plant_cords)

            area = len(plant_cords)
            answer_1 += area * len(fences)

            n_merged_fences = 0
            while fences:
                fx, fy, fdx, fdy = fences.pop()
                if fdx:  # fence is vertical
                    for fy2 in range(fy + 1, h):
                        if (fx, fy2, fdx, fdy) not in fences:
                            break
                        fences.remove((fx, fy2, fdx, fdy))
                    for fy2 in range(fy - 1, -1, -1):
                        if (fx, fy2, fdx, fdy) not in fences:
                            break
                        fences.remove((fx, fy2, fdx, fdy))
                else:  # fence is horizontal
                    for fx2 in range(fx + 1, w):
                        if (fx2, fy, fdx, fdy) not in fences:
                            break
                        fences.remove((fx2, fy, fdx, fdy))
                    for fx2 in range(fx - 1, -1, -1):
                        if (fx2, fy, fdx, fdy) not in fences:
                            break
                        fences.remove((fx2, fy, fdx, fdy))
                n_merged_fences += 1
            answer_2 += area * n_merged_fences

    print(" part 1:", answer_1)
    print(" part 2:", answer_2)


solve("example.txt")  # 1930, 1206
solve("input.txt")  # 1377008, 815788
