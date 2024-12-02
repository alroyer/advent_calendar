from dataclasses import dataclass


@dataclass
class Monkey:
    items: list[int] = None
    operation: str = None
    operation_n: int = -1
    test: int = -1
    on_success: int = -1
    on_failure: int = -1
    inspect: int = 0


def read_data():
    monkeys = {}

    with open('./2022/day11/input1.txt', 'r') as file:
        lines = file.readlines()
        id = -1
        for line in lines:
            if line.startswith('Monkey '):
                id = line[7:].split(':')[0]
                monkeys[id] = Monkey()
            elif line.startswith('  Starting items: '):
                monkeys[id].items = [int(item.strip())
                                     for item in line[18:].split(',')]
            elif line.startswith('  Operation: '):
                operation = line[13:].strip()
                if 'old * old' in operation:
                    monkeys[id].operation = 1
                elif '*' in operation:
                    monkeys[id].operation = 2
                    monkeys[id].operation_n = int(operation[11:])
                else:
                    monkeys[id].operation = 3
                    monkeys[id].operation_n = int(operation[11:])
            elif line.startswith('  Test: divisible by '):
                monkeys[id].test = int(line[21:].strip())
            elif line.startswith('    If true: throw to monkey '):
                monkeys[id].on_success = line[29:].strip()
            elif line.startswith('    If false: throw to monkey '):
                monkeys[id].on_failure = line[30:].strip()

    return monkeys


def main():
    monkeys = read_data()

    for round in range(10000):
        print(f'round {round}')
        for monkey in monkeys.values():
            for item in monkey.items:
                if monkey.operation == 1:
                    item = item * item
                elif monkey.operation == 2:
                    item = item * monkey.operation_n
                else:
                    item = item + monkey.operation_n

                if item % monkey.test == 0:
                    monkeys[monkey.on_success].items.append(item)
                else:
                    monkeys[monkey.on_failure].items.append(item)

                monkey.inspect += 1

            monkey.items = []

    for id, monkey in monkeys.items():
        print(f'Monkey {id} inpected items {monkey.inspect} times')

    x = [monkey.inspect for monkey in monkeys.values()]
    x.sort(reverse=True)
    level = x[0] * x[1]
    print(f'monkey business {level}')


if __name__ == '__main__':
    main()
