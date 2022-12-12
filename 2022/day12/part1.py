def read_data():
    with open('./2022/day12/input1.txt', 'r') as file:
        map = []
        for line in file.readlines():
            map.append([c for c in line.strip()])
        return map


def height_diff(h1, h2):
    if h1 == 'S':
        h1 = 'a'
    elif h1 == 'E':
        h1 = 'z'

    if h2 == 'S':
        h2 = 'a'
    elif h2 == 'E':
        h2 = 'z'

    return ord(h1) - ord(h2)


def main():
    map = read_data()

    column_count = len(map[0])
    row_count = len(map)

    distance_map = []
    for _ in range(row_count):
        distance_map.append([-1 for _ in range(column_count)])

    possible_paths = []

    for y in range(row_count):
        for x in range(column_count):
            if map[y][x] == 'S':
                possible_paths.append((y, x))
                distance_map[y][x] = 0

    while possible_paths:
        pos = possible_paths.pop(0)

        yy = pos[0]
        xx = pos[1]

        current_dist = distance_map[yy][xx]
        next_dist = current_dist + 1

        src = map[yy][xx]

        dy = yy - 1
        dx = xx
        if dy >= 0:
            dst = map[dy][dx]
            height = height_diff(src, dst)
            if height <= 1:
                if distance_map[dy][dx] == -1 or next_dist < distance_map[dy][dx]:
                    distance_map[dy][dx] = next_dist
                    possible_paths.append((dy, dx))

        dy = yy + 1
        dx = xx
        if dy < row_count:
            dst = map[dy][dx]
            height = height_diff(src, dst)
            if height <= 1:
                if distance_map[dy][dx] == -1 or next_dist < distance_map[dy][dx]:
                    distance_map[dy][dx] = next_dist
                    possible_paths.append((dy, dx))

        dy = yy
        dx = xx - 1
        if dx >= 0:
            dst = map[dy][dx]
            height = height_diff(src, dst)
            if height <= 1:
                if distance_map[dy][dx] == -1 or next_dist < distance_map[dy][dx]:
                    distance_map[dy][dx] = next_dist
                    possible_paths.append((dy, dx))

        dy = yy
        dx = xx + 1
        if dx < column_count:
            dst = map[dy][dx]
            height = height_diff(src, dst)
            if height <= 1:
                if distance_map[dy][dx] == -1 or next_dist < distance_map[dy][dx]:
                    distance_map[dy][dx] = next_dist
                    possible_paths.append((dy, dx))

    best = 0
    for y in range(row_count):
        for x in range(column_count):
            best = max(best, distance_map[y][x])
    print(best)


if __name__ == '__main__':
    main()
