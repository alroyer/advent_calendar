# thanks https://gist.github.com/object/c69d0bf44b20cc9b1edb7a9bab5b57d2
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

seconds = 0

while True:
    for robot in robots:
        robot.pos.x = (robot.pos.x + robot.vel.x) % width
        robot.pos.y = (robot.pos.y + robot.vel.y) % height

    seconds += 1

    superpos = False
    points = set()
    for r in robots:
        if r.pos in points:
            superpos = True
            break
        points.add(r.pos)

    if not superpos:
        with open('tree.txt', 'wt') as file:
            for y in range(height):
                for x in range(width):
                    p = Point(x, y)
                    if p in points:
                        file.write('*')
                    else:
                        file.write('.')
                file.write('\n')
        break
