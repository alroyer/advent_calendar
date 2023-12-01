def read_data() -> list[str]:
    with open('input2.txt', 'r') as f:
        calibrationValues = f.readlines()
        return calibrationValues


def compute_calibration_value(line: str) -> int:
    numbers = []
    for c in line:
        if c.isdigit():
            numbers.append(c)
    return int(f'{numbers[0]}{numbers[-1]}')


def main():
    lines = read_data()

    sum = 0
    for line in lines:
        sum = sum + compute_calibration_value(line)

    print(f'{sum=}')


if __name__ == '__main__':
    main()
