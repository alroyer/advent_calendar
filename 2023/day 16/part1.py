with open('input1.txt') as f:
    tiles = [list(tile.strip()) for tile in f.readlines()]

rows = len(tiles)
cols = len(tiles[0])

energized_tiles = []


def travel(beam):
    beams = []

    direction, pos = beam
    row, col = pos

    if row < 0 or row >= rows or col < 0 or col >= cols:
        return []

    if beam in energized_tiles:
        return []

    energized_tiles.append(beam)

    if tiles[row][col] == '.':
        if direction == 'r':
            col += 1
        elif direction == 'l':
            col -= 1
        elif direction == 'd':
            row += 1
        elif direction == 'u':
            row -= 1
        beams.append((direction, (row, col)))
    elif tiles[row][col] == '|':
        if direction in 'rl':
            beams.append(('u', (row - 1, col)))
            beams.append(('d', (row + 1, col)))
        else:
            if direction == 'd':
                row += 1
            elif direction == 'u':
                row -= 1
            beams.append((direction, (row, col)))
    elif tiles[row][col] == '-':
        if direction in 'ud':
            beams.append(('r', (row, col + 1)))
            beams.append(('l', (row, col - 1)))
        else:
            if direction == 'r':
                col += 1
            elif direction == 'l':
                col -= 1
            beams.append((direction, (row, col)))
    elif tiles[row][col] == '/':
        if direction == 'r':
            beams.append(('u', (row - 1, col)))
        elif direction == 'l':
            beams.append(('d', (row + 1, col)))
        elif direction == 'u':
            beams.append(('r', (row, col + 1)))
        elif direction == 'd':
            beams.append(('l', (row, col - 1)))
    elif tiles[row][col] == '\\':
        if direction == 'r':
            beams.append(('d', (row + 1, col)))
        elif direction == 'l':
            beams.append(('u', (row - 1, col)))
        elif direction == 'u':
            beams.append(('l', (row, col - 1)))
        elif direction == 'd':
            beams.append(('r', (row, col + 1)))

    return beams


# for row in range(rows):
#     for col in range(cols):
#         print(tiles[row][col], end='')
#     print()

beams = [('r', (0, 0))]

while beams:
    beam = beams.pop()
    print(beam)

    new_beams = travel(beam)
    if new_beams:
        beams += new_beams

# print(len(energized_tiles))

# for energized_tile in energized_tiles:
#     tiles[energized_tile[1][0]][energized_tile[1][1]] = '#'

# for row in range(rows):
#     for col in range(cols):
#         if tiles[row][col] == '#':
#             print('#', end='')
#         else:
#             print('.', end='')
#     print()

e = set()
for energized_tile in energized_tiles:
    e.add((energized_tile[1][0], energized_tile[1][1]))
print(len(e))
