spelled_numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def read_data() -> list[str]:
    with open('input1.txt', 'r') as f:
        calibrationValues = f.readlines()
        return calibrationValues


def is_spelled_number(line: str) -> tuple[bool, int]:
    for spelled_number in spelled_numbers.items():
        if line.startswith(spelled_number[0]):
            return True, spelled_number[1]
    return False, 0


def compute_calibration_value(line: str) -> int:
    numbers = []
    for index, c in enumerate(line):
        spelled_number, number = is_spelled_number(line[index:])
        if c.isdigit():
            numbers.append(int(c))
        elif spelled_number:
            numbers.append(number)
    return int(f'{numbers[0]}{numbers[-1]}')


def main():
    lines = read_data()

    sum = 0
    for line in lines:
        sum = sum + compute_calibration_value(line)

    print(f'{sum=}')


if __name__ == '__main__':
    main()
