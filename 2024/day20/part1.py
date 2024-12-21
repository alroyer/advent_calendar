from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)


def print_map(height, width, walls, start_pos, end_pos, path):
    for y in range(height):
        for x in range(width):
            point = Point(x, y)
            if point in walls:
                print('#', end='')
            elif point == start_pos:
                print('S', end='')
            elif point == end_pos:
                print('E', end='')
            elif point in path:
                print('O', end='')
            else:
                print('.', end='')
        print()


with open('input0.txt') as f:
    data = f.read().split()

height = len(data)
width = len(data[0])

walls = set()

for y in range(height):
    for x in range(width):
        match data[y][x]:
            case '#':
                walls.add(Point(x, y))
            case 'E':
                end_pos = Point(x, y)
            case 'S':
                start_pos = Point(x, y)

# print_map(height, width, walls, start_pos, end_pos, [])

directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]


def solve(height, width, walls, start_pos, end_pos, max_picoseconds=None):
    to_visite = deque([(start_pos, [])])
    visited = set()

    while to_visite:
        pos, path = to_visite.popleft()

        # if max_picoseconds is not None and len(path) > max_picoseconds:
        #     continue

        if pos == end_pos:
            return len(path)

        for cx, cy in directions:
            cpos = Point(pos.x + cx, pos.y + cy)

            if 0 <= cpos.y < height and 0 <= cpos.x < width and cpos not in walls and cpos not in visited:
                visited.add(cpos)
                to_visite.append((cpos, path + [cpos]))

    return None


max_picoseconds = solve(height, width, walls, start_pos, end_pos)

assert max_picoseconds is not None

cheats = [
    # (-1, 0, (2, width - 1), (1, height - 1)),
    (1, 0, (1, width - 2), (1, height - 1)),
    # (0, -1, (1, width - 1), (2, height - 1)),
    (0, 1, (1, width - 1), (1, height - 2)),
]

count = {}
for cx, cy, (sx, ex), (sy, ey) in cheats:
    for y in range(sy, ey):
        for x in range(sx, ex):
            new_walls = walls.copy()

            if Point(x, y) not in new_walls:
                continue

            new_walls.remove(Point(x, y))

            if Point(x + cx, y + cy) in new_walls:
                new_walls.remove(Point(x + cx, y + cy))

            print_map(height, width, new_walls, start_pos, end_pos, [])

            picoseconds = solve(height, width, new_walls, start_pos, end_pos, max_picoseconds)
            if picoseconds is not None:
                count[max_picoseconds - picoseconds] = count.get(picoseconds, 0) + 1

for k, v in count.items():
    if v == 1:
        print(f'There is one cheat that saves {k} picoseconds.')
    else:
        print(f'There are {v} cheats that save {k} picoseconds.')
