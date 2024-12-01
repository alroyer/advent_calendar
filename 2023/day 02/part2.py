def read_data(path: str) -> list[str]:
    with open(path, 'r') as f:
        data = f.readlines()
        return data


def parse_data(data: list[str]) -> int:
    sum = 0
    for game in data:
        _, all_sets = game.split(':')
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
        sets = all_sets.split(';')
        for s in sets:
            cubes = s.split(',')
            for c in cubes:
                count, color = c.split()
                min_cubes[color] = max(min_cubes[color], int(count))
        power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
        sum = sum + power
    return sum


def main() -> None:
    data = read_data('input1.txt')

    sum = parse_data(data)
    print(f'{sum=}')


if __name__ == '__main__':
    main()
