def is_symbol(c: str) -> bool:
    return c == '*'


def read_data(path: str) -> list[str]:
    with open(path, 'r') as f:
        data = []
        line = f.readline()
        while line:
            data.append(line.strip())
            line = f.readline()
        return data


def find_part_numbers(data: list[str], visited: list[tuple[int, int]], y: int, x: int) -> list[int]:
    part_numbers = []
    for cy in range(y - 1, y + 2):
        for cx in range(x - 1, x + 2):
            if cy >= 0 and cy < len(data) and cx >= 0 and cx <= len(data[cy]):
                if data[cy][cx].isdigit() and (cy, cx) not in visited:
                    xx = cx
                    while xx > 0 and data[cy][xx].isdigit() and (cy, xx) not in visited:
                        visited.append((cy, xx))
                        xx -= 1
                    if not data[cy][xx].isdigit():
                        xx += 1
                    number = ''
                    while xx < len(data[cy]) and data[cy][xx].isdigit():
                        number = number + data[cy][xx]
                        if (cy, xx) not in visited:
                            visited.append((cy, xx))
                        xx += 1
                    part_numbers.append(int(number))
    return part_numbers if len(part_numbers) == 2 else []


def parse_data(data: list[str]) -> int:
    sum = 0
    visited = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if is_symbol(data[y][x]):
                part_numbers = find_part_numbers(data, visited, y, x)
                if part_numbers:
                    gear_ratio = part_numbers[0] * part_numbers[1]
                    sum = sum + gear_ratio
    return sum


def main() -> None:
    data = read_data('input1.txt')

    sum = parse_data(data)
    print(f'{sum=}')


if __name__ == '__main__':
    main()
