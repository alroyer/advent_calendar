def read_data(path: str) -> list[str]:
    with open(path, 'r') as f:
        data = []
        line = f.readline()
        while line:
            data.append(line.strip())
            line = f.readline()
        return data


def compute_total(data: list[str]) -> int:
    gen = {}
    for card in data:
        card_number, numbers = card.split(':')
        card_number = int(card_number[5:])
        winning_numbers, your_numbers = numbers.split('|')
        winning_numbers = list(filter(None, winning_numbers.split(' ')))
        your_numbers = list(filter(None, your_numbers.split(' ')))
        count = 0
        for your_number in your_numbers:
            if your_number in winning_numbers:
                count += 1
        gen[card_number] = [card_number + n + 1 for n in range(count)]
    return 0


def main() -> None:
    data = read_data('input0.txt')
    total = compute_total(data)
    print(f'{total=}')


if __name__ == '__main__':
    main()
