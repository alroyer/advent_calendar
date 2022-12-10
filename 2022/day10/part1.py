def read_data():
    with open('./2022/day10/input2.txt', 'r') as file:
        return file.readlines()


def main():
    instructions = read_data()

    cycles = {}
    index = 0

    for instruction in instructions:
        if instruction.startswith('noop'):
            index += 1
            cycles[index] = instruction
        elif instruction.startswith('addx'):
            index += 2
            cycles[index] = instruction

    max_cycle = max(cycles.keys())

    signals = []
    for n in range(20, max_cycle, 40):
        signals.append(n)

    sum_signal_strenght = 0
    X = 1
    for cycle in range(1, max_cycle + 1):
        if cycle in signals:
            signal_strenght = cycle * X
            sum_signal_strenght += signal_strenght
            print(cycle, X, signal_strenght)

        if cycle in cycles:
            instruction = cycles[cycle]
            if instruction.startswith('addx'):
                X += int(instruction.split()[1])

    print(sum_signal_strenght)


if __name__ == '__main__':
    main()
