from dataclasses import dataclass
from copy import copy
from typing import Tuple
import heapq


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
                print('X', end='')
            else:
                print('.', end='')
        print()


def compute_score(p1: Point, p2: Point, direction: Tuple[int, int]):
    score = 1
    new_direction = (p2.x - p1.x, p2.y - p1.y)
    if new_direction != direction:
        score += 1000
    return score, new_direction


with open('input2.txt') as f:
    data = f.read().split()

height = len(data)
width = len(data[0])

walls = set()

start_pos = None
end_pos = None

for y in range(height):
    for x in range(width):
        match data[y][x]:
            case '#':
                walls.add(Point(x, y))
            case 'E':
                end_pos = Point(x, y)
            case 'S':
                start_pos = Point(x, y)

assert start_pos

# print_map(height, width, walls, start_pos, end_pos)

paths = []

directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

current_direction = (-1, 0)

visited = set()
to_visite = [(0, start_pos, current_direction)]

while to_visite:
    score, pos, direction = heapq.heappop(to_visite)

    if pos == end_pos:
        break

    visited.add(pos)

    for cx, cy in directions:
        cpos = Point(pos.x + cx, pos.y + cy)
        if cpos in walls or cpos in visited:
            continue
        new_score, new_direction = compute_score(cpos, pos, direction)
        heapq.heappush(to_visite, (score + new_score, cpos, new_direction))

print(score)
