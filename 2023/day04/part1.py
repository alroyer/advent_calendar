def read_data(path: str) -> list[str]:
    with open(path, 'r') as f:
        data = []
        line = f.readline()
        while line:
            data.append(line.strip())
            line = f.readline()
        return data


def compute_point(data: list[str]) -> int:
    point = 0
    for card in data:
        _, numbers = card.split(':')
        winning_numbers, your_numbers = numbers.split('|')
        winning_numbers = list(filter(None, winning_numbers.split(' ')))
        your_numbers = list(filter(None, your_numbers.split(' ')))
        count = 0
        for your_number in your_numbers:
            if your_number in winning_numbers:
                count += 1
        point = point + 2 ** (count - 1) if count > 0 else point
    return point


def main() -> None:
    data = read_data('input1.txt')
    point = compute_point(data)
    print(f'{point=}')


if __name__ == '__main__':
    main()
