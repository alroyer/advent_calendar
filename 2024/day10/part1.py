def print_map(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            print(map[y][x], end='')
        print()


with open('input5.txt') as f:
    data = f.read()

map = list(data.split())

# print_map(map)

trailheads = []

height = len(map)
width = len(map[0])

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

total_score = 0

for y in range(height):
    for x in range(width):
        if map[y][x] == '0':
            positions = [(y, x, 0)]
            visited = set()
            score = 0
            while positions:
                py, px, h = positions.pop()
                for cy, cx in directions:
                    yy = py + cy
                    xx = px + cx
                    if yy >= 0 and yy < height and xx >= 0 and xx < width:
                        try:
                            hh = int(map[yy][xx])
                            if hh == h + 1:
                                if hh == 9:
                                    if (yy, xx) not in visited:
                                        score += 1
                                        visited.add((yy, xx))
                                else:
                                    positions.append((yy, xx, hh))

                        except:
                            pass
            total_score += score

print(total_score)
