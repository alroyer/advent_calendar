with open('input0.txt', 'r') as f:
    data = f.read().split('\n')

height = len(data)
width = len(data[0])

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
    data.insert(row, width * '.')

for col in reversed(cols):
    for index, row in enumerate(data):
        new_row = row[:col] + '.' + row[col:]
        data[index] = new_row

# for row in data:
#     print(row)

# compute galaxies pair

height = len(data)
width = len(data[0])

galaxies = []
for y in range(height):
    for x in range(width):
        if data[y][x] == '#':
            galaxies.append((y, x))

print(galaxies)

pairs = [(a, b) for index, a in enumerate(galaxies) for b in galaxies[index + 1 :]]

distances = []
for a, b in pairs:
    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
    distances.append(distance)
print(sum(distances))
