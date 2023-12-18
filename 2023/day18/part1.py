directions = {
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
    'U': (-1, 0),
}

dig_plan = []
with open('input1.txt') as f:
    for line in f.readlines():
        direction, count, color = line.strip().split(' ')
        dig_plan.append((direction, int(count), color))

trenchs = set()

x1, x2 = 0, 0
y1, y2 = 0, 0

pos = (0, 0)
for direction, count, _ in dig_plan:
    for n in range(count):
        pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
        trenchs.add(pos)

        x1 = min(x1, pos[1])
        x2 = max(x2, pos[1])

        y1 = min(y1, pos[0])
        y2 = max(y2, pos[0])

height = (y2 - y1) + 1
width = (x2 - x1) + 1

plan = []

for i in range(height):
    plan.append([])
    for j in range(width):
        if (i + y1, j + x1) in trenchs:
            plan[i].append('#')
        else:
            plan[i].append('.')

# cheat
p = []
p.append((1, 229))
seen = []
while p:
    y, x = p.pop()
    seen.append((y, x))
    plan[y][x] = '#'
    for direction in directions.values():
        yy = y + direction[0]
        xx = x + direction[1]
        if yy >= 0 and yy < height and xx >= 0 and xx < width and plan[yy][xx] == '.' and (yy, xx) not in seen:
            p.append((yy, xx))


with open('out.txt', 'w') as f:
    count = 0
    for i in range(height):
        for j in range(width):
            if plan[i][j] != '.':
                count += 1
            f.write(plan[i][j])
        f.write('\n')
    print(count)
