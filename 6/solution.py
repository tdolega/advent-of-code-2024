WALL = "#"
EMPTY = "."
START = "^"
DIRECTIONS = [
    (0, -1),  # up
    (1, 0),  # right
    (0, 1),  # down
    (-1, 0),  # left
]


def get_start_pos(obstructions_map: list[str]):
    for y, line in enumerate(obstructions_map):
        for x, char in enumerate(line):
            if char == START:
                return x, y, 0


def create_tracking_map(width: int, height: int, directions: int = 4):
    return [[[False] * directions for _ in range(width)] for _ in range(height)]


def mark_and_check_loop(tracking_map: list[list[list[bool]]], x: int, y: int, direction: int):
    if tracking_map[y][x][direction]:
        return True  # detected loop
    tracking_map[y][x][direction] = True
    return False


def step(obstructions_map: list[str], x: int, y: int, direction: int):
    for direction_offset in range(4):
        next_direction = (direction + direction_offset) % len(DIRECTIONS)
        x_offset, y_offset = DIRECTIONS[next_direction]
        next_x = x + x_offset
        next_y = y + y_offset
        if next_x < 0 or next_x >= len(obstructions_map[0]) or next_y < 0 or next_y >= len(obstructions_map):
            return False
        if obstructions_map[next_y][next_x] != WALL:
            return next_x, next_y, next_direction
    raise ValueError("No valid step found")


def solve(filename: str):
    print(filename)
    with open(filename) as f:
        obstructions_map = list(map(list, f.read().splitlines()))

    w, h = len(obstructions_map[0]), len(obstructions_map)
    tracking_map = create_tracking_map(w, h)
    first_step = get_start_pos(obstructions_map)
    next_step = first_step
    while next_step:
        x, y, direction = next_step
        mark_and_check_loop(tracking_map, x, y, direction)
        next_step = step(obstructions_map, x, y, direction)
    visited_map = [[sum(directions) > 0 for directions in row] for row in tracking_map]

    answer_1 = 0
    answer_2 = 0
    for obstruction_x in range(w):
        for obstruction_y in range(h):
            if not visited_map[obstruction_y][obstruction_x]:
                continue
            answer_1 += 1

            obstructions_map[obstruction_y][obstruction_x] = WALL
            tracking_map = create_tracking_map(w, h)
            next_step = first_step
            while next_step:
                x, y, direction = next_step
                if mark_and_check_loop(tracking_map, x, y, direction):
                    answer_2 += 1
                    break
                next_step = step(obstructions_map, x, y, direction)
            obstructions_map[obstruction_y][obstruction_x] = EMPTY

    print(f" part 1: {answer_1}")
    print(f" part 2: {answer_2}")


solve("example.txt")  # 41, 6
solve("input.txt")  # 4433, 1516
