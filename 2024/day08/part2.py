from dataclasses import dataclass


@dataclass(frozen=True)
class Pos:
    x: int
    y: int


def diff(p1, p2):
    return p2.x - p1.x, p2.y - p1.y


with open('input1.txt') as f:
    data = f.read()

map = data.split()

h = len(map)
w = len(map[0])

antennas = {}

for y in range(h):
    for x in range(w):
        m = map[y][x]
        if m != '.':
            if m not in antennas:
                antennas[m] = []
            antennas[m].append(Pos(x, y))

antinodes = set()

for antenna, pos in antennas.items():
    for p1 in pos:
        for p2 in pos:
            if p1 == p2:
                continue
            cx, cy = diff(p1, p2)
            antinode = Pos(p1.x + cx, p1.y + cy)
            while antinode.x >= 0 and antinode.x < w and antinode.y >= 0 and antinode.y < h:
                antinodes.add(antinode)
                antinode = Pos(antinode.x + cx, antinode.y + cy)

print(len(antinodes))
