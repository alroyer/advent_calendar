from dataclasses import dataclass
from collections import deque


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def print_map(height, width, walls, start_pos, end_pos, path):
    for y in range(height):
        for x in range(width):
            point = Point(x, y)
            if point in walls:
                print('#', end='')
            elif point == start_pos:
                print('O', end='')
            # elif point == end_pos:
            #     print('E', end='')
            elif point in path:
                print('O', end='')
            else:
                print('.', end='')
        print()


with open('input1.txt') as f:
    data = [d.replace('\n', '') for d in f.readlines()]

bytes = 1024
falling_bytes = []
for d in data:
    x, y = d.split(',')
    falling_bytes.append(Point(int(x), int(y)))
falling_bytes = falling_bytes[:bytes]

height = 71
width = 71

start_pos = Point(0, 0)
end_pos = Point(width - 1, height - 1)

# print_map(height, width, falling_bytes, start_pos, end_pos, [])

directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

to_visite = deque([(start_pos, [])])
visited = set()

while to_visite:
    pos, path = to_visite.popleft()

    if pos == end_pos:
        print(len(path))
        break

    for cx, cy in directions:
        cpos = Point(pos.x + cx, pos.y + cy)

        if 0 <= cpos.y < height and 0 <= cpos.x < width and cpos not in falling_bytes and cpos not in visited:
            visited.add(cpos)
            to_visite.append((cpos, path + [cpos]))

print_map(height, width, falling_bytes[:bytes], start_pos, end_pos, path)
