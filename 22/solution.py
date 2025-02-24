N_ITERATIONS = 2000


def mix(secret: int, value: int):
    return secret ^ value


def prune(secret: int):
    return secret % 16777216


def evolve(secret: int):
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret


def evolve_n(secret: int, n: int):
    history = [secret]
    for _ in range(n):
        secret = evolve(secret)
        history.append(secret)
    return history


def sequence_to_price(secret_history: list[int]):
    sequences = {}
    sequence = (None, None, None, None)
    last_price = 0
    for secret in secret_history:
        price = secret % 10
        price_diff = price - last_price
        last_price = price
        sequence = sequence[1:] + (price_diff,)
        if None in sequence:
            continue
        if sequence not in sequences:
            sequences[sequence] = price
    return sequences


def solve(filename: str):
    print(filename)
    with open(filename, "r") as f:
        initial_secrets = map(int, f.read().splitlines())

    secret_histories = [evolve_n(secret, N_ITERATIONS) for secret in initial_secrets]
    print(" part 1:", sum(secret_history[-1] for secret_history in secret_histories))

    sequence_maps = [sequence_to_price(secret_history) for secret_history in secret_histories]
    all_sequences = set(sequence for sequence_map in sequence_maps for sequence in sequence_map.keys())

    max_price = 0
    for sequence in all_sequences:
        total_price = 0
        for sequence_map in sequence_maps:
            total_price += sequence_map.get(sequence, 0)
        max_price = max(max_price, total_price)
    print(" part 2:", max_price)


solve("example.txt")  # 37327623, -
solve("example2.txt")  # -, 23
solve("input.txt")  # 12664695565, 1444
