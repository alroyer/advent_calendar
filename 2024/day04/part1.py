with open('input2.txt') as f:
    data = f.read()

total = 0

dir = [
    (-1, -1),
    (1, -1),
    (-1, 1),
    (1, 1),
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]
w = 'MAS'
s = data.split()
total = 0

height = len(s)
width = len(s[0])

for y in range(height):
    for x in range(width):
        if s[y][x] == 'X':
            for d in dir:
                index = 0
                yy = y + d[0]
                xx = x + d[1]
                while index < len(w) and yy >= 0 and xx >= 0 and yy < height and xx < width:
                    if s[yy][xx] != w[index]:
                        break
                    yy += d[0]
                    xx += d[1]
                    index += 1
                if index == len(w):
                    total += 1

print(total)
