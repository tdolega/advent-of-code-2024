def solve(filename: str):
    print(filename)
    with open(filename) as f:
        rows = (map(int, line.split()) for line in f)
        lcol, rcol = zip(*rows)

    lcol, rcol = sorted(lcol), sorted(rcol)
    distance_sum = sum(abs(l - r) for l, r in zip(lcol, rcol))
    print(f" part 1: {distance_sum}")

    n_l_in_r = map(rcol.count, lcol)
    similarity_score = sum(l * r for l, r in zip(lcol, n_l_in_r))
    print(f" part 2: {similarity_score}")


solve("example.txt")  # 11, 31
solve("input.txt")  # 1882714, 19437052
