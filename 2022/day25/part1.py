def read_data():
    with open('./2022/day25/input1.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]


def snafu_to_decimal(snafu_number):
    decimal = 0
    for index, c in enumerate(snafu_number):
        pos = (len(snafu_number) - index) - 1
        if c == '2':
            decimal += 5**pos * 2
        elif c == '1':
            decimal += 5**pos
        elif c == '0':
            continue
        elif c == '=':
            decimal -= 5**pos * 2
        elif c == '-':
            decimal -= 5**pos
    return decimal


def decimal_to_snafu(decimal):
    encode = '012=-'
    res = ''
    while decimal:
        res += encode[decimal % 5]
        if decimal > 2:
            decimal += 2
        decimal //= 5
    return res[::-1]


def main():
    data = read_data()
    print(data)

    numbers = [snafu_to_decimal(number) for number in data]
    print(numbers)

    sum_decimal = sum(numbers)
    print(sum_decimal)

    snafu_sum = decimal_to_snafu(sum_decimal)
    print(snafu_sum)


if __name__ == "__main__":
    main()
