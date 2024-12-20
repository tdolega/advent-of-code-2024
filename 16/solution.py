WALL = "#"
EMPTY = "."
START = "S"
END = "E"
COST_MOVE = 1
COST_ROTATE = 1000


def get_cord(grid: list[str], tile: str):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == tile:
                return x, y


def solve(filename: str):
    print(filename)
    with open(filename) as f:
        grid = f.read().splitlines()

    min_paths = set()
    min_cost = float("inf")
    cost_to_reach_cord = {}
    start_x, start_y = get_cord(grid, START)
    to_check = [((start_x, start_y), [(start_x - 1, start_y)], 0)]  # path starts at the west of the start, because we have to face east
    while to_check:
        (x, y), path, cost = to_check.pop(0)

        if cost > min_cost:  # this path can't be better than the best one we already have
            continue

        tile = grid[y][x]
        if tile == WALL or (x, y) in path:
            continue
        if tile == END:
            if cost < min_cost:
                min_cost = cost
                min_paths = set()
            min_paths.update(path)
            continue

        min_cost_to_this = cost_to_reach_cord.get((x, y), float("inf"))
        if min_cost_to_this < cost - COST_ROTATE:  # we have to subtract COST_ROTATE, because there might be different path that will reach this cord with the same cost after it rotates here in next step
            continue
        if min_cost_to_this > cost:
            cost_to_reach_cord[(x, y)] = cost

        px, py = path[-1]
        path = path + [(x, y)]
        to_check.append(((2 * x - px, 2 * y - py), path, cost + COST_MOVE))
        if px == x:
            to_check.append(((x - 1, y), path, cost + COST_MOVE + COST_ROTATE))
            to_check.append(((x + 1, y), path, cost + COST_MOVE + COST_ROTATE))
        else:
            to_check.append(((x, y - 1), path, cost + COST_MOVE + COST_ROTATE))
            to_check.append(((x, y + 1), path, cost + COST_MOVE + COST_ROTATE))

    print(" part 1:", min_cost)
    # min_paths has one extra element at the start but at the same time it's missing the last element, so length is the same
    print(" part 2:", len(min_paths))


solve("example.txt")  # 7036, 45
solve("example2.txt")  # 11048, 64
solve("input.txt")  # 91464, 494
