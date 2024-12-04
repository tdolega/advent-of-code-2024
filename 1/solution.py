with open("input1.txt") as f:
    rows = [list(map(int, line.split())) for line in f]
    columns = list(zip(*rows))
    lcol, rcol = columns
lcol, rcol = sorted(lcol), sorted(rcol)
distance_sum = sum(abs(l - r) for l, r in zip(lcol, rcol))
print(f"solution 1: {distance_sum}")  # 1882714

n_l_in_r = map(rcol.count, lcol)
similarity_score = sum(l * r for l, r in zip(lcol, n_l_in_r))
print(f"solution 2: {similarity_score}")  # 19437052
