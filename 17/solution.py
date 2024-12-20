import re

INPUT_REGEX = r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: ((?:\d+,?)+)"


class Opcodes:
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


def parse(filename: str):
    print(filename)
    with open(filename, "r") as f:
        match = re.match(INPUT_REGEX, f.read())
    ra, rb, rc = map(int, match.group(1, 2, 3))
    program = list(map(int, match.group(4).split(",")))
    return ra, rb, rc, program


def run(ra: int, rb: int, rc: int, program: list[int]):
    def combo(operand: int):
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return ra
            case 5:
                return rb
            case 6:
                return rc
        raise ValueError(f"invalid operand '{operand}'")

    output = []
    ip = 0
    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]
        ip += 2

        match opcode:
            case Opcodes.BXL:
                rb ^= operand
            case Opcodes.BXC:
                rb ^= rc
            case Opcodes.BST:
                rb = combo(operand) % 8
            case Opcodes.OUT:
                output.append(combo(operand) % 8)
            case Opcodes.ADV:
                ra = ra // 2 ** combo(operand)
            case Opcodes.BDV:
                rb = ra // 2 ** combo(operand)
            case Opcodes.CDV:
                rc = ra // 2 ** combo(operand)
            case Opcodes.JNZ:
                if ra != 0:
                    ip = operand

    return output


def solve_1(filename: str):
    ra, rb, rc, program = parse(filename)
    answer = run(ra, rb, rc, program)
    answer = ",".join(map(str, answer))
    print(" part 1:", answer)


def solve_2(filename: str):
    _, rb, rc, program = parse(filename)
    multipliers = [0] * len(program)
    for idx in reversed(range(len(program))):
        # changing ra by 8**i controls the i-th digit, so we can find the solution by checking all possible i values, starting from the least significant digit
        while True:
            ra = sum(multiplier * 8**i for i, multiplier in enumerate(multipliers))
            output = run(ra, rb, rc, program)
            if output[idx:] == program[idx:]:
                break
            multipliers[idx] += 1
    print(" part 2:", ra)


solve_1("example.txt")  # 4,6,3,5,6,3,5,2,1,0
solve_2("example2.txt")  # 117440
solve_1("input.txt")  # 7,1,3,4,1,2,6,7,1
solve_2("input.txt")  # 109019476330651
