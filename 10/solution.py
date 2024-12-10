START_LEVEL = 0
END_LEVEL = 9


def starting_positions(topo_map: list[list[int]]):
    positions = []
    for y in range(len(topo_map)):
        for x in range(len(topo_map[y])):
            if topo_map[y][x] == START_LEVEL:
                positions.append((x, y))
    return positions


def get_end_positions(topo_map: list[list[int]], visited: dict, last_x: int, last_y: int, x: int, y: int):
    if x < 0 or y < 0 or x >= len(topo_map[0]) or y >= len(topo_map):
        return []  # out of bounds

    current_level = topo_map[y][x]
    last_level = topo_map[last_y][last_x]
    if current_level != last_level + 1 and len(visited):
        return []  # not a valid move

    prev_positions = visited.setdefault((x, y), [])
    prev_positions.append((last_x, last_y))
    if len(prev_positions) > 1:
        return []  # already explored

    if current_level == END_LEVEL:
        return [(x, y)]  # reached the end

    end_positions = []
    end_positions += get_end_positions(topo_map, visited, x, y, x + 1, y)
    end_positions += get_end_positions(topo_map, visited, x, y, x - 1, y)
    end_positions += get_end_positions(topo_map, visited, x, y, x, y + 1)
    end_positions += get_end_positions(topo_map, visited, x, y, x, y - 1)
    return end_positions


def solve(filename: str):
    print(filename)
    with open(filename, "r") as f:
        topo_map = [list(map(int, line)) for line in f.read().splitlines()]

    n_end_positions = 0
    n_branches = 0
    for start_x, start_y in starting_positions(topo_map):
        visited = {}
        positions = get_end_positions(topo_map, visited, start_x, start_y, start_x, start_y)
        n_end_positions += len(positions)

        visited[(start_x, start_y)] = []  # first position is a loop
        while positions:  # count branches from the end using BFS
            position = positions.pop()
            if prev_positions := visited[position]:
                n_branches += len(prev_positions) - 1
                positions.extend(prev_positions)

    print(" part 1:", n_end_positions)
    print(" part 2:", n_end_positions + n_branches)


solve("example.txt")  # 36, 81
solve("input.txt")  # 629, 1242
