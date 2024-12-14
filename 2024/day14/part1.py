import re
from dataclasses import dataclass
from functools import reduce
from operator import mul


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash(self.x) + hash(self.y)


@dataclass
class Robot:
    pos: Point
    vel: Point


with open('input1.txt') as f:
    data = f.read().split('\n')

robots = []
p = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
for d in data:
    m = p.match(d)
    if not m:
        continue
    pos = Point(int(m.group(1)), int(m.group(2)))
    vel = Point(int(m.group(3)), int(m.group(4)))
    robots.append(Robot(pos, vel))

height = 103
width = 101

seconds = 100

for robot in robots:
    robot.pos.x = (robot.pos.x + (robot.vel.x * seconds)) % width
    robot.pos.y = (robot.pos.y + (robot.vel.y * seconds)) % height

quadrants = [
    ((0, 0), (width // 2 - 1, height // 2 - 1)),
    ((width // 2 + 1, 0), (width - 1, height // 2 - 1)),
    ((0, height // 2 + 1), (width // 2 - 1, height - 1)),
    ((width // 2 + 1, height // 2 + 1), (width - 1, height - 1)),
]

count = []
for n, quadrant in enumerate(quadrants):
    r = list(
        filter(
            lambda r: r.pos.x >= quadrant[0][0]
            and r.pos.x <= quadrant[1][0]
            and r.pos.y >= quadrant[0][1]
            and r.pos.y <= quadrant[1][1],
            robots,
        )
    )
    count.append(len(r))
print(reduce(mul, count))

# points = {}
# for r in robots:
#     if r.pos not in points:
#         points[r.pos] = 0
#     points[r.pos] += 1

# for y in range(height):
#     for x in range(width):
#         p = Point(x, y)
#         if p in points:
#             print(points[p], end='')
#         else:
#             print('.', end='')
#     print()
