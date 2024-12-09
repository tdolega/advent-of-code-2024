def checksum(disk: list[int]):
    return sum(i * block_id for i, block_id in enumerate(disk) if block_id != None)


def solve_1(disk: list[int]):
    left = 0
    right = len(disk) - 1
    while True:
        while disk[left] != None:
            left += 1
        while disk[right] == None:
            right -= 1
        if left >= right:
            break
        disk[left], disk[right] = disk[right], disk[left]
    return disk


# return pointers to first block from the right, return None if not found
def find_block(disk: list[int]):
    right = len(disk) - 1
    while right >= 0 and disk[right] == None:
        right -= 1
    left = right
    while disk[left] == disk[right]:
        left -= 1
        if left < 0:
            return None
    return left + 1, right + 1


# return pointers to empty space of size from the left, return None if not found
def find_empty(disk: list[int], size: int):
    left = right = 0
    while left < len(disk):
        while left < len(disk) and disk[left] != None:
            left += 1
        right = left
        while right < len(disk) and disk[right] == None:
            right += 1
            if right - left == size:
                return left, right
        left = right
    return None


def solve_2(disk: list[int]):
    block_right = len(disk)
    while block_found := find_block(disk[:block_right]):
        block_left, block_right = block_found
        size = block_right - block_left
        if empty_found := find_empty(disk[:block_left], size):
            empty_left, empty_right = empty_found
            disk[empty_left:empty_right] = disk[block_left:block_right]
            disk[block_left:block_right] = [None] * size
        block_right = block_left
    return disk


def solve(filename: str):
    print(filename)
    with open(filename, "r") as f:
        disk_map = map(int, f.read().strip())

    disk = []
    for i, length in enumerate(disk_map):
        block_id = i // 2 if i % 2 == 0 else None
        disk.extend([block_id] * length)

    print(" part 1:", checksum(solve_1(disk.copy())))
    print(" part 2:", checksum(solve_2(disk.copy())))


solve("example.txt")  # 1928, 2858
solve("input.txt")  # 6461289671426, 6488291456470
