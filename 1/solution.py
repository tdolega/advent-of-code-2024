with open("input.txt") as f:
    rows = (map(int, line.split()) for line in f)
    lcol, rcol = zip(*rows)

lcol, rcol = sorted(lcol), sorted(rcol)
distance_sum = sum(abs(l - r) for l, r in zip(lcol, rcol))
print(f"part 1: {distance_sum}")  # 1882714

n_l_in_r = map(rcol.count, lcol)
similarity_score = sum(l * r for l, r in zip(lcol, n_l_in_r))
print(f"part 2: {similarity_score}")  # 19437052
