EMPTY = "."
CORRUPTED = "#"


def shortest_path_length(memory: list[list[str]]):
    w, h = len(memory[0]), len(memory)
    end_cords = (w - 1, h - 1)
    visited = set()
    queue = [(0, 0, 0)]
    while queue:
        x, y, steps = queue.pop(0)
        if (x, y) == end_cords:
            return steps
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and memory[ny][nx] == EMPTY:
                queue.append((nx, ny, steps + 1))
    return None  # no path


def solve(filename: str, size: int, milliseconds: int):
    print(filename)
    with open(filename, "r") as f:
        positions = [map(int, line.split(",")) for line in f.readlines()]

    memory = [[EMPTY] * size for _ in range(size)]
    for x, y in positions[:milliseconds]:
        memory[y][x] = CORRUPTED

    print(" part 1:", shortest_path_length(memory))

    for x, y in positions[milliseconds:]:
        memory[y][x] = CORRUPTED
        if not shortest_path_length(memory):
            print(" part 2:", f"{x},{y}")
            break


solve("example.txt", 6 + 1, 12)  # 22, 6,1
solve("input.txt", 70 + 1, 1024)  # 262, 22,20
