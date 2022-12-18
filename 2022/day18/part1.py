def read_data():
    with open('./2022/day18/input1.txt', 'r') as file:
        cube_positions = []
        for line in file.readlines():
            x, y, z = line.split(',')
            cube_positions.append((int(x), int(y), int(z)))
        return cube_positions


def main():
    cube_positions = read_data()
    # print(cube_positions)

    total_sides = 6 * len(cube_positions)
    # print(total_sides)

    connected_sides = 0
    for cube1 in cube_positions:
        for cube2 in cube_positions:
            x1 = cube1[0]
            x2 = cube2[0]

            y1 = cube1[1]
            y2 = cube2[1]

            z1 = cube1[2]
            z2 = cube2[2]

            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            dz = abs(z1 - z2)

            if dx + dy + dz == 1:
                connected_sides += 1
    # print(connected_sides)

    exposed_sides = total_sides - connected_sides
    print(f'exposed sides: {exposed_sides}')


if __name__ == '__main__':
    main()
