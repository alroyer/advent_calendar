from dataclasses import dataclass


@dataclass
class Monkey:
    items: list[int] = None
    operation: str = None
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
                monkeys[id].operation = line[13:].strip()
            elif line.startswith('  Test: divisible by '):
                monkeys[id].test = int(line[21:].strip())
            elif line.startswith('    If true: throw to monkey '):
                monkeys[id].on_success = line[29:].strip()
            elif line.startswith('    If false: throw to monkey '):
                monkeys[id].on_failure = line[30:].strip()

    return monkeys


def main():
    monkeys = read_data()

    for _ in range(20):
        for monkey in monkeys.values():
            for item in monkey.items:
                if 'old * old' in monkey.operation:
                    item = int(item * item / 3)
                elif '*' in monkey.operation:
                    item = int(item * int(monkey.operation[11:]) / 3)
                else:
                    item = int((item + int(monkey.operation[11:])) / 3)

                if item % monkey.test == 0:
                    monkeys[monkey.on_success].items.append(item)
                    # print(
                    #     f'item {item} is thrown to monkey {monkey.on_success}')
                else:
                    monkeys[monkey.on_failure].items.append(item)
                    # print(
                    #     f'item {item} is thrown to monkey {monkey.on_failure}')

                monkey.inspect += 1

            monkey.items = []

    # for monkey in monkeys.values():
    #     print(monkey.items)

    # for monkey in monkeys.values():
    #     print(monkey.inspect)

    x = [monkey.inspect for monkey in monkeys.values()]
    x.sort(reverse=True)

    level = x[0] * x[1]
    print(level)


if __name__ == '__main__':
    main()
