def read_data():
    map = []
    with open('./2022/day8/input1.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            map.append([int(h) for h in line.strip()])
    return map


def compute_viewing_distance(map):
    viewing_distance = []
    for y in range(len(map)):
        viewing_distance.append([])
        for x in range(len(map[y])):
            viewing_distance[y].append(0)

    for y in range(1, len(map) - 1):
        for x in range(1, len(map[y]) - 1):
            h = map[y][x]

            left = 0
            xx = x - 1
            while xx >= 0:
                if map[y][xx] >= h:
                    left += 1
                    break
                else:
                    left += 1
                xx -= 1

            right = 0
            xx = x + 1
            while xx < len(map[y]):
                if map[y][xx] >= h:
                    right += 1
                    break
                else:
                    right += 1
                xx += 1

            top = 0
            yy = y - 1
            while yy >= 0:
                if map[yy][x] >= h:
                    top += 1
                    break
                else:
                    top += 1
                yy -= 1

            bottom = 0
            yy = y + 1
            while yy < len(map):
                if map[yy][x] >= h:
                    bottom += 1
                    break
                else:
                    bottom += 1
                yy += 1

            viewing_distance[y][x] = left * right * top * bottom

    return viewing_distance


def main():
    map = read_data()
    viewing_distances = compute_viewing_distance(map)

    highest = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            highest = max(highest, viewing_distances[y][x])
    print(highest)


if __name__ == '__main__':
    main()
