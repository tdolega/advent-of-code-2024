sum2 = lambda x, y: x + y
mul2 = lambda x, y: x * y
concat2 = lambda x, y: int(f"{x}{y}")


def is_correct(result: int, numbers: list[int], operations: tuple[callable], prev: int = 0):
    if len(numbers) == 0:
        return result == prev

    first, rest = numbers[0], numbers[1:]
    return any(is_correct(result, rest, operations, op(prev, first)) for op in operations)


def solve(filename: str):
    part_1 = part_2 = 0
    with open(filename, "r") as f:
        print(filename)
        for line in f.readlines():
            result, *numbers = line.split()
            result = int(result[:-1])
            numbers = list(map(int, numbers))
            if is_correct(result, numbers, (sum2, mul2)):
                part_1 += result
            if is_correct(result, numbers, (sum2, mul2, concat2)):
                part_2 += result

    print(" part 1:", part_1)
    print(" part 2:", part_2)


solve("example.txt")  # 3749, 11387
solve("input.txt")  # 4364915411363, 38322057216320
