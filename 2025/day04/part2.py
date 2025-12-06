# diagram = [
#     "..@@.@@@@.",
#     "@@@.@.@.@@",
#     "@@@@@.@.@@",
#     "@.@@@@..@.",
#     "@@.@@@@.@@",
#     ".@@@@@@@.@",
#     ".@.@.@.@@@",
#     "@.@@@.@@@@",
#     ".@@@@@@@@.",
#     "@.@.@@@.@.",
# ]

with open("input1.txt") as f:
    diagram = [line.strip() for line in f.readlines()]

count = 0
last_count = -1

while last_count != count:
    last_count = count

    pos = []
    for y in range(0, len(diagram)):
        for x in range(0, len(diagram[y])):
            rolls_count = 0
            if diagram[y][x] == ".":
                continue
            for cy in range(-1, 2):
                for cx in range(-1, 2):
                    if cx == 0 and cy == 0:
                        continue
                    yy = y + cy
                    xx = x + cx
                    if yy < 0 or yy >= len(diagram) or xx < 0 or xx >= len(diagram[yy]):
                        continue
                    if diagram[y + cy][x + cx] == "@":
                        rolls_count += 1
            if rolls_count < 4:
                count += 1
                pos.append((y, x))
    for p in pos:
        diagram[p[0]] = diagram[p[0]][: p[1]] + "." + diagram[p[0]][p[1] + 1 :]

print(count)
