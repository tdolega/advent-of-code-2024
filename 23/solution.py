import networkx as nx


def solve(filename: str):
    print(filename)

    G = nx.Graph()
    with open(filename, "r") as f:
        for line in f:
            a, b = line.strip().split("-")
            G.add_edge(a, b)

    answer_1 = 0
    largest_clique = []
    for clique in nx.enumerate_all_cliques(G):
        largest_clique = clique  # enumerate_all_cliques is sorted
        if len(clique) == 3 and any(computer.startswith("t") for computer in clique):
            answer_1 += 1

    print(" part 1:", answer_1)
    print(" part 2:", ",".join(sorted(largest_clique)))


solve("example.txt")  # 7, co,de,ka,ta
solve("input.txt")  # 1304, ao,es,fe,if,in,io,ky,qq,rd,rn,rv,vc,vl
