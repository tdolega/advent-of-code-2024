WALL = "#"
SMALL_BOX = "O"
BIG_BOX_L = "["
BIG_BOX_R = "]"
EMPTY = "."
ROBOT = "@"

MOVE_TO_DIRECTION = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}


def locate_robot(warehouse: list[list[str]]):
    for y, line in enumerate(warehouse):
        for x, cell in enumerate(line):
            if cell == ROBOT:
                return x, y


def gps_score(warehouse: list[list[str]]):
    answer = 0
    for y, line in enumerate(warehouse):
        for x, cell in enumerate(line):
            if cell == SMALL_BOX or cell == BIG_BOX_L:
                answer += 100 * y + x
    return answer


def can_move(warehouse: list[list[str]], x: int, y: int, dx: int, dy: int, log: dict):
    next_x, next_y = x + dx, y + dy

    if (x, y) in log:
        return True
    log[(x, y)] = (next_x, next_y, warehouse[y][x])

    next_tile = warehouse[next_y][next_x]
    if next_tile == SMALL_BOX:
        return can_move(warehouse, next_x, next_y, dx, dy, log)
    if next_tile == BIG_BOX_L:
        return can_move(warehouse, next_x, next_y, dx, dy, log) and can_move(warehouse, next_x + 1, next_y, dx, dy, log)
    if next_tile == BIG_BOX_R:
        return can_move(warehouse, next_x, next_y, dx, dy, log) and can_move(warehouse, next_x - 1, next_y, dx, dy, log)
    return next_tile != WALL


def solve_any(warehouse: list[list[str]], moves: str):
    warehouse = list(map(list, warehouse.splitlines()))
    robot_x, robot_y = locate_robot(warehouse)
    for move in moves:
        if move == "\n":
            continue
        dx, dy = MOVE_TO_DIRECTION[move]
        log = {}
        if can_move(warehouse, robot_x, robot_y, dx, dy, log):
            for x, y in log.keys():
                warehouse[y][x] = EMPTY
            for x, y, tile in log.values():
                warehouse[y][x] = tile
            robot_x += dx
            robot_y += dy
    return gps_score(warehouse)


def solve(filename: str):
    print(filename)
    with open(filename, "r") as file:
        warehouse, moves = file.read().split("\n\n")

    print(" part 1:", solve_any(warehouse, moves))

    warehouse = warehouse.translate(
        str.maketrans(
            {
                WALL: WALL + WALL,
                SMALL_BOX: BIG_BOX_L + BIG_BOX_R,
                EMPTY: EMPTY + EMPTY,
                ROBOT: ROBOT + EMPTY,
            }
        )
    )
    print(" part 2:", solve_any(warehouse, moves))


solve("example.txt")  # 10092, 9021
solve("input.txt")  # 1515788, 1516544
