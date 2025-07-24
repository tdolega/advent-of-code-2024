def overlap(height: int, lock: list[int], key: list[int]):
    for li, ki in zip(lock, key):
        if li + ki >= height - 1:
            return True
    return False

def solve(filename: str):
    print(filename)
    with open(filename, "r") as file:
        locks_and_keys = file.read().strip().split("\n\n")

    locks = []
    keys = []
    for lock_or_key in locks_and_keys:
        grid = lock_or_key.split("\n")
        width = len(grid[0])
        height = len(grid)

        pins = []
        for x in range(width):
            pin = -1
            for y in range(height):
                if grid[y][x] == "#":
                    pin += 1
            pins.append(pin)

        if grid[0][0] == "#":
            locks.append(pins)
        else:
            keys.append(pins)

    fit = 0
    for lock in locks:
        for key in keys:
            if not overlap(height, lock, key):
                fit += 1
    print(" part 1:", fit)


solve("example.txt")  # 3
solve("input.txt")  # 2770
