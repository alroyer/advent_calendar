import re
from dataclasses import dataclass


@dataclass
class Machine:
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize: tuple[int, int]


def func(machine):
    solutions = []
    for i in range(100):
        for j in range(100):
            x1 = machine.button_a[0]
            x2 = machine.button_b[0]

            y1 = machine.button_a[1]
            y2 = machine.button_b[1]

            r1 = machine.prize[0]
            r2 = machine.prize[1]

            if (x1 * i + x2 * j) == r1 and (y1 * i + y2 * j) == r2:
                solutions.append((i, j, i + j))

    if solutions:
        x = min(solutions, key=lambda x: x[2])
        return x[0], x[1]

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
    prize = (int(m.group(1)), int(m.group(2)))

    machines.append(Machine(button_a, button_b, prize))

total = 0
for machine in machines:
    result = func(machine)
    if result:
        ax, bx = result
        total += ax * 3 + bx
print(total)
