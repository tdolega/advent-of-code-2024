from sympy import symbols, Eq, solve, diophantine
import re

COST_A = 3
COST_B = 1
MACHINE_REGEX = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"


def solve_diofantine(ax: int, ay: int, bx: int, by: int, px: int, py: int):
    a, b = symbols("a b", integer=True)
    eq1 = Eq(ay * a + by * b, py)
    eq2 = Eq(ax * a + bx * b, px)

    # eliminate a
    eq1_scaled = Eq(ax * (ay * a + by * b), ax * py)
    eq2_scaled = Eq(ay * (ax * a + bx * b), ay * px)
    eliminated = eq1_scaled.lhs - eq2_scaled.lhs
    rhs = eq1_scaled.rhs - eq2_scaled.rhs
    eq_b = Eq(eliminated, rhs)

    # solve for b
    b_solutions = diophantine(eq_b)

    for b_vals in b_solutions:
        b_val = b_vals[0]
        # solve for a
        a_vals = solve(eq1.subs(b, b_val), a)
        if a_vals:
            return a_vals[0], b_val
    return None


def solve_part(machines: list[list[str]], prize_error: int):
    answer = 0
    for machine in machines:
        ax, ay, bx, by, px, py = map(int, machine)
        if solution := solve_diofantine(ax, ay, bx, by, px + prize_error, py + prize_error):
            a, b = solution
            answer += a * COST_A + b * COST_B
    return answer


def solve_both(filename: str):
    print(filename)
    with open(filename) as f:
        machines = re.findall(MACHINE_REGEX, f.read())

    print(" part 1:", solve_part(machines, 0))
    print(" part 2:", solve_part(machines, 10000000000000))


solve_both("example.txt")  # 480
solve_both("input.txt")  # 27157, 104015411578548
