from dataclasses import dataclass
from copy import copy


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def print_map(m):
    h = len(map)
    w = len(map[0])
    for y in range(h):
        for x in range(w):
            print(map[y][x], end='')
        print()


def print_all(h, w, walls, boxes, robot):
    for y in range(h):
        for x in range(w):
            p = Point(x, y)
            if p in walls:
                print('#', end='')
            elif p in boxes:
                print('O', end='')
            elif p == robot:
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


def get_boxes(walls, boxes, pos, move):
    boxes_to_move = []
    box_pos = copy(pos)
    while box_pos in boxes:
        boxes_to_move.append(box_pos)
        box_pos = get_next_pos(box_pos, move)
        if box_pos in walls:
            return None
    return boxes_to_move


with open('input3.txt') as f:
    data = f.read()

map = list(filter(lambda d: '#' in d, data.split()))
moves = list(filter(lambda d: '<' in d, data.split()))[0]

walls = set()
boxes = set()

height = len(map)
width = len(map[0])

for y in range(height):
    for x in range(width):
        match map[y][x]:
            case '#':
                walls.add(Point(x, y))
            case 'O':
                boxes.add(Point(x, y))
            case '@':
                robot_pos = Point(x, y)

for move in moves:
    next_pos = get_next_pos(robot_pos, move)
    if next_pos in walls:
        continue
    elif next_pos in boxes:
        boxes_to_move = get_boxes(walls, boxes, next_pos, move)
        if not boxes_to_move:
            continue
        boxes.add(get_next_pos(boxes_to_move[-1], move))
        boxes.remove(boxes_to_move[0])
        robot_pos = next_pos
    else:
        robot_pos = next_pos

print_all(height, width, walls, boxes, robot_pos)

total = 0
for box in boxes:
    total += 100 * box.y + box.x
print(1413675, total)
