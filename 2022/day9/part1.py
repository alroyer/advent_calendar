from dataclasses import dataclass


def read_data():
    with open('./2022/day9/input1.txt', 'r') as file:
        lines = file.readlines()
        moves = []
        for line in lines:
            direction, count = line.split()
            moves.append((direction, int(count)))
        return moves


@dataclass
class Position:
    x: int
    y: int


def main():
    head_position = Position(x=0, y=0)
    tail_position = Position(x=0, y=0)

    visited = set()

    moves = read_data()
    for direction, count in moves:
        for _ in range(count):
            if direction == 'R':
                head_position.x += 1
            elif direction == 'L':
                head_position.x -= 1
            elif direction == 'U':
                head_position.y -= 1
            elif direction == 'D':
                head_position.y += 1

            dx = abs(head_position.x - tail_position.x)
            dy = abs(head_position.y - tail_position.y)

            # horizontal
            if dx > 1 and dy == 0:
                tail_position.x += 1 if (head_position.x -
                                         tail_position.x) > 0 else -1
            # vertical
            elif dy > 1 and dx == 0:
                tail_position.y += 1 if (head_position.y -
                                         tail_position.y) > 0 else -1

            # diags
            if (dx > 1 and dy == 1) or (dy > 1 and dx == 1):
                tail_position.x += 1 if (head_position.x -
                                         tail_position.x) > 0 else -1
                tail_position.y += 1 if (head_position.y -
                                         tail_position.y) > 0 else -1

            visited.add((tail_position.x, tail_position.y))

    # print(head_position)
    # print(tail_position)

    print(len(visited))


if __name__ == '__main__':
    main()
