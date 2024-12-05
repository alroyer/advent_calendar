with open('input2.txt') as f:
    data = f.read()

total = 0

s = data.split()
total = 0

height = len(s)
width = len(s[0])

for y in range(1, height - 1):
    for x in range(1, width - 1):
        if s[y][x] == 'A':
            if (s[y - 1][x - 1] == 'M' and s[y + 1][x - 1] == 'M') and (
                s[y - 1][x + 1] == 'S' and s[y + 1][x + 1] == 'S'
            ):
                total += 1
            elif (s[y - 1][x - 1] == 'S' and s[y + 1][x - 1] == 'S') and (
                s[y - 1][x + 1] == 'M' and s[y + 1][x + 1] == 'M'
            ):
                total += 1
            elif (s[y - 1][x - 1] == 'S' and s[y + 1][x - 1] == 'M') and (
                s[y - 1][x + 1] == 'S' and s[y + 1][x + 1] == 'M'
            ):
                total += 1
            elif (s[y - 1][x - 1] == 'M' and s[y + 1][x - 1] == 'S') and (
                s[y - 1][x + 1] == 'M' and s[y + 1][x + 1] == 'S'
            ):
                total += 1

print(total)
