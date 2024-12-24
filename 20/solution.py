START = "S"
END = "E"
TRACK = "."
WALL = "#"


def get_xy(racetrack: list[str], tile: str):
    for y, row in enumerate(racetrack):
        for x, cell in enumerate(row):
            if cell == tile:
                return x, y


def waterfall_to_xy(racetrack: list[str], x: int, y: int):
    w, h = len(racetrack[0]), len(racetrack)
    distances = [[float("inf") for _ in range(w)] for _ in range(h)]
    distances[y][x] = 0
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= w or ny < 0 or ny >= h or racetrack[ny][nx] == WALL or distances[ny][nx] != float("inf"):
                continue
            distances[ny][nx] = distances[y][x] + 1
            stack.append((nx, ny))
    return distances


def distances_with_skip(distances_to_start: list[list[int]], distances_to_end: list[list[int]], max_skip: int):
    w, h = len(distances_to_end[0]), len(distances_to_end)
    improved_distances = []
    for y in range(h):
        for x in range(w):
            distance_to_start = distances_to_start[y][x]
            distance_to_end = distances_to_end[y][x]
            if distance_to_start == float("inf") or distance_to_end == float("inf"):
                continue
            for dx in range(-max_skip, max_skip + 1):
                for dy in range(-max_skip, max_skip + 1):
                    n_skipped = abs(dx) + abs(dy)
                    if n_skipped > max_skip:
                        continue
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= w or ny < 0 or ny >= h:
                        continue
                    distance_to_end_after_skip = distances_to_end[ny][nx]
                    total_distance_without_skip = distance_to_start + distance_to_end
                    total_distance_with_skip = distance_to_start + n_skipped + distance_to_end_after_skip
                    if total_distance_with_skip < total_distance_without_skip:
                        improved_distances.append(total_distance_with_skip)
    return improved_distances


def answer(racetrack: list[str], max_skip: int, count_under_margin: int = 100):
    start_x, start_y = get_xy(racetrack, START)
    end_x, end_y = get_xy(racetrack, END)

    distances_to_start = waterfall_to_xy(racetrack, start_x, start_y)
    distances_to_end = waterfall_to_xy(racetrack, end_x, end_y)

    distance_without_skip = distances_to_end[start_y][start_x]
    distances_with_skips = distances_with_skip(distances_to_start, distances_to_end, max_skip)

    return len([d for d in distances_with_skips if d <= distance_without_skip - count_under_margin])


def solve(filename: str):
    print(filename)
    with open(filename) as f:
        racetrack = f.read().splitlines()
    print(" part 1:", answer(racetrack, 2))
    print(" part 2:", answer(racetrack, 20))


solve("example.txt")  # 0, 0
solve("input.txt")  # 1395, 993178
