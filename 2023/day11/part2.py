with open('input1.txt', 'r') as f:
    data = f.read().split('\n')

expand = 1000000 - 1

height = len(data)
width = len(data[0])

galaxies = []
for y in range(height):
    for x in range(width):
        if data[y][x] == '#':
            galaxies.append((y, x))

# expand the universe

rows = []
for index, row in enumerate(data):
    if not '#' in row:
        rows.append(index)

cols = []
for x in range(width):
    cc = []
    for y in range(height):
        cc.append(data[y][x])
    if not '#' in cc:
        cols.append(x)

for row in reversed(rows):
    for index, galaxy in enumerate(galaxies):
        if galaxy[0] > row:
            galaxies[index] = (galaxy[0] + expand, galaxy[1])

for col in reversed(cols):
    for index, galaxy in enumerate(galaxies):
        if galaxy[1] > col:
            galaxies[index] = (galaxy[0], galaxy[1] + expand)

# print(galaxies)

# compute galaxies pair

pairs = [(a, b) for index, a in enumerate(galaxies) for b in galaxies[index + 1 :]]

# compute distances

distances = []
for a, b in pairs:
    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
    distances.append(distance)

print(sum(distances))
