def read_data():
    map = []
    with open('./2022/day8/input1.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            map.append([int(h) for h in line.strip()])
    return map


def find_visible_trees(map):
    visible_trees = []
    for y in range(len(map)):
        visible_trees.append([])
        for x in range(len(map[y])):
            if x == 0 or x == len(map[y]) - 1 or y == 0 or y == len(map) - 1:
                visible_trees[y].append(1)
            else:
                visible_trees[y].append(0)

    for y in range(1, len(map) - 1):
        for x in range(1, len(map[y]) - 1):
            h = map[y][x]

            # left
            visible = True
            xx = x - 1
            while xx >= 0 and visible:
                if map[y][xx] >= h:
                    visible = False
                xx -= 1
            if visible:
                visible_trees[y][x] = 1

            # right
            visible = True
            xx = x + 1
            while xx < len(map[y]) and visible:
                if map[y][xx] >= h:
                    visible = False
                xx += 1
            if visible:
                visible_trees[y][x] = 1

            # top
            visible = True
            yy = y - 1
            while yy >= 0 and visible:
                if map[yy][x] >= h:
                    visible = False
                yy -= 1
            if visible:
                visible_trees[y][x] = 1

            # bottom
            visible = True
            yy = y + 1
            while yy < len(map) and visible:
                if map[yy][x] >= h:
                    visible = False
                yy += 1
            if visible:
                visible_trees[y][x] = 1

    return visible_trees


def main():
    map = read_data()
    visible_trees = find_visible_trees(map)

    sum = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if visible_trees[y][x] == 1:
                sum += 1
    print(sum)


if __name__ == '__main__':
    main()
