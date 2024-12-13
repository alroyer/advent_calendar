import re
from dataclasses import dataclass
from sympy import symbols, Eq, solve


@dataclass
class Machine:
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize: tuple[int, int]


def func(machine):
    A1 = machine.button_a[0]
    A2 = machine.button_a[1]
    B1 = machine.button_b[0]
    B2 = machine.button_b[1]
    R1 = machine.prize[0]
    R2 = machine.prize[1]

    x, y = symbols('x y')

    eq1 = Eq(A1 * x + B1 * y, R1)
    eq2 = Eq(A2 * x + B2 * y, R2)

    solution = solve((eq1, eq2), (x, y))
    if solution:
        x = int(solution[x])
        y = int(solution[y])

        if (A1 * x + B1 * y == R1) and (A2 * x + B2 * y == R2):
            return x, y

    return None


with open('input1.txt') as f:
    data = f.read().split('\n')

ba_re = re.compile(r'Button A: X\+(\d+), Y\+(\d+)')
bb_re = re.compile(r'Button B: X\+(\d+), Y\+(\d+)')
prize_re = re.compile(r'Prize: X=(\d+), Y=(\d+)')

machines = []
for index in range(0, len(data), 4):
    m = ba_re.match(data[index])
    if not m:
        continue
    button_a = (int(m.group(1)), int(m.group(2)))
    m = bb_re.match(data[index + 1])
    if not m:
        continue
    button_b = (int(m.group(1)), int(m.group(2)))
    m = prize_re.match(data[index + 2])
    if not m:
        continue
    prize = (int(m.group(1)) + 10000000000000, int(m.group(2)) + 10000000000000)

    machines.append(Machine(button_a, button_b, prize))

total = 0
for machine in machines:
    result = func(machine)
    if result:
        ax, bx = result
        total += ax * 3 + bx
print(total)
