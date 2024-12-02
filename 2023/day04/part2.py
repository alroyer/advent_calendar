def read_data(path: str) -> list[str]:
    with open(path, 'r') as f:
        data = []
        line = f.readline()
        while line:
            data.append(line.strip())
            line = f.readline()
        return data


def compute_total(data: list[str]) -> int:
    win = {}
    for card in data:
        card_number, numbers = card.split(':')
        card_number = int(card_number[5:])
        winning_numbers, your_numbers = numbers.split('|')
        winning_numbers = list(filter(None, winning_numbers.split(' ')))
        your_numbers = list(filter(None, your_numbers.split(' ')))
        total = 0
        for your_number in your_numbers:
            if your_number in winning_numbers:
                total += 1
        win[card_number] = [card_number + n + 1 for n in range(total)]

    total = {}
    for card_number, copies in win.items():
        if card_number in total:
            total[card_number] += 1
        else:
            total[card_number] = 1
        for copy in copies:
            if copy in total:
                total[copy] = total[copy] + total[card_number]
            else:
                total[copy] = 1
    return sum(total.values())


def main() -> None:
    data = read_data('input0.txt')
    total = compute_total(data)
    print(f'{total=}')


if __name__ == '__main__':
    main()
