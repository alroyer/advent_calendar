PIPES = {
    '-': ((0, 1), (0, -1)),  # east, weast
    '|': ((-1, 0), (1, 0)),  # north, south
    'L': ((-1, 0), (0, 1)),  # north, east
    'J': ((-1, 0), (0, -1)),  # north, weast
    '7': ((1, 0), (0, -1)),  # south, weast
    'F': ((1, 0), (0, 1)),  # south, east
}

with open('input2.txt', 'r') as f:
    sketch = f.read().split('\n')

start = None
nodes = {}
for y, row in enumerate(sketch):
    for x, col in enumerate(row):
        src = (y, x)
        p = sketch[y][x]
        if p in PIPES:
            for d in PIPES[p]:
                dst = (y + d[0], x + d[1])
                if src in nodes:
                    nodes[src].append(dst)
                else:
                    nodes[src] = [dst]
        elif p == 'S':
            start = (y, x)

start_dst = []
for src, dst in nodes.items():
    if start in dst:
        start_dst.append(src)
nodes[start] = start_dst

height = len(sketch)
width = len(sketch[0])

distances = []
for _ in range(height):
    distances.append(width * [-1])
if start:
    distances[start[0]][start[1]] = 0

visite = [start]
visited = []
long = 0

while visite:
    src = visite.pop()
    assert src
    visited.append(src)
    for dst in nodes[src]:
        if not dst in visited:
            visite.insert(0, dst)
            distance = distances[src[0]][src[1]] + 1
            distances[dst[0]][dst[1]] = distance
            long = max(long, distance)

# for row in distances:
#     print(row)

print(long)
