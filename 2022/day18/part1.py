def read_data():
    with open('./2022/day18/input1.txt', 'r') as file:
        cube_positions = []
        for line in file.readlines():
            x, y, z = line.split(',')
            cube_positions.append((int(x), int(y), int(z)))
        return cube_positions


def main():
    cube_positions = read_data()

    total_sides = 6 * len(cube_positions)

    connected_sides = 0
    for cube1 in cube_positions:
        for cube2 in cube_positions:
            dx = abs(cube1[0] - cube2[0])
            dy = abs(cube1[1] - cube2[1])
            dz = abs(cube1[2] - cube2[2])

            if dx + dy + dz == 1:
                connected_sides += 1

    exposed_sides = total_sides - connected_sides
    print(f'exposed sides: {exposed_sides}')


if __name__ == '__main__':
    main()
