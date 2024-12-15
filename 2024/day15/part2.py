from dataclasses import dataclass
from copy import copy


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True)
class Box:
    pos: Point
    face: str


def print_all(walls, boxes, robot_pos, height, width):
    for y in range(height):
        for x in range(width):
            p = Point(x, y)
            if p in walls:
                print('#', end='')
            elif p in boxes:
                print(boxes[p], end='')
            elif p == robot_pos:
                print('@', end='')
            else:
                print('.', end='')
        print()


def get_next_pos(pos, move):
    match move:
        case '<':
            return Point(pos.x - 1, pos.y)
        case '>':
            return Point(pos.x + 1, pos.y)
        case '^':
            return Point(pos.x, pos.y - 1)
        case 'v':
            return Point(pos.x, pos.y + 1)


def get_boxes_to_move(walls, boxes, pos, move):
    visited = set()
    boxes_to_move = []
    pos_to_check = [pos]
    while pos_to_check:
        p = pos_to_check.pop()
        if p in visited:
            continue
        visited.add(p)
        if p in walls:
            return None
        elif p in boxes:
            if move == '^' or move == 'v':
                if boxes[p] == ']':
                    pp = Point(p.x - 1, p.y)
                    if pp in visited:
                        continue
                    visited.add(pp)
                    boxes_to_move.append(Box(pp, '['))
                    pos_to_check.append(get_next_pos(pp, move))
                else:
                    pp = Point(p.x + 1, p.y)
                    if pp in visited:
                        continue
                    visited.add(pp)
                    boxes_to_move.append(Box(pp, ']'))
                    pos_to_check.append(get_next_pos(pp, move))
            boxes_to_move.append(Box(p, boxes[p]))
            pos_to_check.append(get_next_pos(p, move))
    return boxes_to_move


def resize_map(map):
    walls = set()
    boxes = {}

    height = len(map)
    width = len(map[0])

    for y in range(height):
        for x in range(width):
            match map[y][x]:
                case '#':
                    walls.add(Point(x * 2, y))
                    walls.add(Point(x * 2 + 1, y))
                case 'O':
                    boxes[Point(x * 2, y)] = '['
                    boxes[Point(x * 2 + 1, y)] = ']'
                case '@':
                    robot_pos = Point(x * 2, y)
    return walls, boxes, robot_pos, height, width * 2


with open('input3.txt') as f:
    data = f.read()

map = list(filter(lambda d: '#' in d, data.split()))
moves = list(filter(lambda d: '<' in d, data.split()))[0]

walls, boxes, robot_pos, height, width = resize_map(map)

for move in moves:
    next_pos = get_next_pos(robot_pos, move)
    if next_pos in walls:
        continue
    elif next_pos in boxes:
        boxes_to_move = get_boxes_to_move(walls, boxes, next_pos, move)
        if not boxes_to_move:
            continue
        if move == '<' or move == '>':
            for box in reversed(boxes_to_move):
                boxes[get_next_pos(box.pos, move)] = box.face
            del boxes[boxes_to_move[0].pos]
        else:
            for box in reversed(boxes_to_move):
                boxes[get_next_pos(box.pos, move)] = box.face
                del boxes[box.pos]
        robot_pos = next_pos
    else:
        robot_pos = next_pos

    # print(move)
    # print_all(walls, boxes, robot_pos, height, width)

total = 0
for pos, face in boxes.items():
    if face == '[':
        total += 100 * pos.y + pos.x
print(total)
