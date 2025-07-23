operations = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "XOR": lambda x, y: x ^ y,
}


def solve_1(gates: dict[str, tuple[str, str, str]], wires: dict[str, int]):
    gates = gates.copy()
    while gates:
        for output_wire_name, (operation, input1_wire_name, input2_wire_name) in gates.items():
            input1_wire = wires.get(input1_wire_name)
            input2_wire = wires.get(input2_wire_name)
            if input1_wire is not None and input2_wire is not None:
                wires[output_wire_name] = operations[operation](input1_wire, input2_wire)
                gates.pop(output_wire_name)
                break

    sorted_z_wires = sorted([wire for wire in wires if wire.startswith("z")], reverse=True)
    answer_bin = "".join(str(wires[wire]) for wire in sorted_z_wires)
    answer_dec = int(answer_bin, 2)
    print(" part 1:", answer_dec)


def solve_2(gates: dict[str, tuple[str, str, str]], _):
    input_size = max(int(wire[1:]) for wire in gates.keys() if wire.startswith("z"))

    def wire_name(char: str, i: int):
        return f"{char}{i:02}"

    null_values = {}
    for i in range(input_size):
        null_values[wire_name("x", i)] = 0
        null_values[wire_name("y", i)] = 0

    def init_values(i: int, x: int, y: int, carry: int):
        x_values = {wire_name("x", i): x, wire_name("x", i - 1): carry}
        y_values = {wire_name("y", i): y, wire_name("y", i - 1): carry}
        return null_values | x_values | y_values

    def get_value(wire: str, values: dict[str, int]):
        if wire in values:
            return values[wire]
        operation, input1_wire_name, input2_wire_name = gates[wire]
        values[wire] = operations[operation](get_value(input1_wire_name, values), get_value(input2_wire_name, values))
        return values[wire]

    def find_wire(op1: str, ins1: set[str]):
        for out, (op2, *ins2) in gates.items():
            if op1 == op2 and ins1.issubset(set(ins2)):
                return out

    def fix_bit(i: int):
        curr_x, curr_y = wire_name("x", i), wire_name("y", i)
        prev_x, prev_y = wire_name("x", i - 1), wire_name("y", i - 1)
        curr_xor = find_wire("XOR", {curr_x, curr_y})
        prev_xor = find_wire("XOR", {prev_x, prev_y})
        direct_carry = find_wire("AND", {prev_x, prev_y})
        recarry = find_wire("AND", {prev_xor})
        carry = find_wire("OR", {direct_carry, recarry})
        z = find_wire("XOR", {curr_xor, carry})
        if z is None:
            z_ins = set(gates[wire_name("z", i)][1:])
            w1, w2 = z_ins ^ {curr_xor, carry}
        else:
            w1, w2 = {z, wire_name("z", i)}
        gates[w1], gates[w2] = gates[w2], gates[w1]
        return {w1, w2}

    swapped_wires_names = set()
    for i in range(1, input_size):
        if any(x ^ y ^ c != get_value(wire_name("z", i), init_values(i, x, y, c)) for x in range(2) for y in range(2) for c in range(2)):
            swapped_wires_names |= fix_bit(i)

    answer = ",".join(sorted(swapped_wires_names))
    print(" part 2:", answer)
    assert answer == "cph,jqn,kwb,qkf,tgr,z12,z16,z24"


def parse(filename: str):
    print(filename)
    with open(filename, "r") as f:
        input_wires, input_gates = f.read().split("\n\n")

    wires = {}
    for line in input_wires.strip().split("\n"):
        wire_name, value = line.split(": ")
        wires[wire_name] = int(value)

    gates = {}
    for line in input_gates.strip().split("\n"):
        input1_wire_name, operation, input2_wire_name, _, output_wire_name = line.split()
        gates[output_wire_name] = (operation, input1_wire_name, input2_wire_name)

    return gates, wires


solve_1(*parse("example.txt"))  # 4
solve_1(*parse("example2.txt"))  # 2024
parsed = parse("input.txt")
solve_1(*parsed)  # 52038112429798
solve_2(*parsed)  # cph,jqn,kwb,qkf,tgr,z12,z16,z24
