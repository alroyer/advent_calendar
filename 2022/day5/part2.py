from dataclasses import dataclass
import re


@dataclass
class Move:
    count: int
    from_stack: int
    to_stack: int


def read_data():
    # input0
    # stacks = [
    #     ['Z', 'N'],
    #     ['M', 'C', 'D'],
    #     ['P']
    # ]
    # input1
    stacks = [
        ['Q', 'W', 'P', 'S', 'Z', 'R', 'H', 'D'],
        ['V', 'B', 'R', 'W', 'Q', 'H', 'F'],
        ['C', 'V', 'S', 'H'],
        ['H', 'F', 'G'],
        ['P', 'G', 'J', 'B', 'Z'],
        ['Q', 'T', 'J', 'H', 'W', 'F', 'L'],
        ['Z', 'T', 'W', 'D', 'L', 'V', 'J', 'N'],
        ['D', 'T', 'Z', 'C', 'J', 'G', 'H', 'F'],
        ['W', 'P', 'V', 'M', 'B', 'H'],
    ]
    moves = []

    with open('./2022/day5/input1.txt', 'r') as file:
        lines = file.readlines()
        is_a_move = False
        for line in lines:
            if not line.strip():
                is_a_move = True
            elif is_a_move:
                m = re.search('move (\d+) from (\d+) to (\d+)', line)
                moves.append(Move(int(m.group(1)), int(
                    m.group(2))-1, int(m.group(3))-1))
            else:
                pass
    return stacks, moves


def main():
    stacks, moves = read_data()

    for move in moves:
        crates = stacks[move.from_stack][-move.count:]
        # crates.reverse()

        stacks[move.from_stack] = stacks[move.from_stack][:-move.count]
        stacks[move.to_stack] += crates

    # print(stacks)

    for stack in stacks:
        print(stack)


if __name__ == '__main__':
    main()
