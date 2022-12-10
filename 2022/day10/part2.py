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

    X = 1
    cycle = 1
    for y in range(6):
        for x in range(0, 40):
            if X in range(x-1, x+2):
                print('##', end='')
            else:
                print('  ', end='')

            if cycle in cycles:
                instruction = cycles[cycle]
                if instruction.startswith('addx'):
                    X += int(instruction.split()[1])
            cycle += 1

        print()


if __name__ == '__main__':
    main()
