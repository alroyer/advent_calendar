from dataclasses import dataclass


def read_data():
    with open('./2022/day9/input2.txt', 'r') as file:
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
    tail_position = [Position(x=0, y=0) for _ in range(11)]

    visited = set()

    moves = read_data()
    for direction, count in moves:
        for _ in range(count):
            if direction == 'R':
                tail_position[0].x += 1
            elif direction == 'L':
                tail_position[0].x -= 1
            elif direction == 'U':
                tail_position[0].y -= 1
            elif direction == 'D':
                tail_position[0].y += 1

            for index in range(1, 11):
                dx = abs(tail_position[index - 1].x - tail_position[index].x)
                dy = abs(tail_position[index - 1].y - tail_position[index].y)

                # horizontal
                if dx > 1 and dy == 0:
                    tail_position[index].x += 1 if (tail_position[index - 1].x -
                                                    tail_position[index].x) > 0 else -1
                # vertical
                elif dy > 1 and dx == 0:
                    tail_position[index].y += 1 if (tail_position[index - 1].y -
                                                    tail_position[index].y) > 0 else -1

                # diags
                if (dx > 1 and dy == 1) or (dy > 1 and dx == 1) or (dx > 1 and dy > 1):
                    tail_position[index].x += 1 if (tail_position[index - 1].x -
                                                    tail_position[index].x) > 0 else -1
                    tail_position[index].y += 1 if (tail_position[index - 1].y -
                                                    tail_position[index].y) > 0 else -1

            visited.add((tail_position[10].x, tail_position[10].y))

    print(len(visited))


if __name__ == '__main__':
    main()
