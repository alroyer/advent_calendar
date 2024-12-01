MAX_CUBES = {'red': 12, 'green': 13, 'blue': 14}


def read_data(path: str) -> list[str]:
    with open(path, 'r') as f:
        data = f.readlines()
        return data


def parse_data(data: list[str]) -> int:
    sum = 0

    for game in data:
        id, all_sets = game.split(':')
        possible = True
        sets = all_sets.split(';')
        for s in sets:
            cubes = s.split(',')
            for c in cubes:
                count, color = c.split()
                if int(count) > MAX_CUBES[color.strip()]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            sum = sum + int(id[5:])

    return sum


def main() -> None:
    data = read_data('input1.txt')

    sum = parse_data(data)
    print(f'{sum=}')


if __name__ == '__main__':
    main()
