from dataclasses import dataclass


@dataclass
class Pos:
    x: int
    y: int
    dir: int = 0  # 0=up, 1=right, 2=down, 3=right

    def turn_right(self):
        self.dir += 1
        self.dir = self.dir % 4

    def next_move(self):
        if self.dir == 0:
            return Pos(y=self.y - 1, x=self.x)
        elif self.dir == 1:
            return Pos(y=self.y, x=self.x + 1)
        elif self.dir == 2:
            return Pos(y=self.y + 1, x=self.x)
        else:
            return Pos(y=self.y, x=self.x - 1)

    def move_to(self, pos):
        self.y = pos.y
        self.x = pos.x

    def __hash__(self):
        return hash((self.y, self.x))


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

visited = set()

while pos.y >= 0 and pos.y < h and pos.x >= 0 and pos.x < w:
    visited.add(pos)
    new_pos = pos.next_move()
    if new_pos.y < 0 or new_pos.y >= h or new_pos.x < 0 or new_pos.x >= w:
        break
    if map[new_pos.y][new_pos.x] == '#':
        pos.turn_right()
    else:
        pos.move_to(new_pos)

print(len(visited))
