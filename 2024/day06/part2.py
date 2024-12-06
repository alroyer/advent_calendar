from copy import copy
from dataclasses import dataclass


@dataclass(frozen=True)
class Pos:
    x: int
    y: int
    dir: int = 0  # 0=up, 1=right, 2=down, 3=right

    def turn_right(self):
        return Pos(self.x, self.y, (self.dir + 1) % 4)

    def next_move(self):
        if self.dir == 0:
            return Pos(y=self.y - 1, x=self.x, dir=0)
        elif self.dir == 1:
            return Pos(y=self.y, x=self.x + 1, dir=1)
        elif self.dir == 2:
            return Pos(y=self.y + 1, x=self.x, dir=2)
        else:
            return Pos(y=self.y, x=self.x - 1, dir=3)


with open('input1.txt') as f:
    data = f.read()

map = data.split()

h = len(map)
w = len(map[0])

pos = None

for y in range(h):
    for x in range(w):
        if map[y][x] == '^':
            pos = Pos(x=x, y=y, dir=0)

assert pos is not None

total = 0
start = copy(pos)

for y in range(h):
    for x in range(w):
        new_map = map.copy()
        if new_map[y][x] == '#' or new_map[y][x] == '^':
            continue
        new_map[y] = new_map[y][:x] + '#' + new_map[y][x + 1 :]
        visited = set()
        pos = copy(start)
        while pos.y >= 0 and pos.y < h and pos.x >= 0 and pos.x < w:
            if pos in visited:
                total += 1
                break
            visited.add(pos)
            new_pos = pos.next_move()
            if new_pos.y < 0 or new_pos.y >= h or new_pos.x < 0 or new_pos.x >= w:
                break
            if new_map[new_pos.y][new_pos.x] == '#':
                pos = pos.turn_right()
            else:
                pos = new_pos

print(total)
