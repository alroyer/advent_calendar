def parse(reports):
    assert reports

    bits = [0] * (len(reports[0]) - 1)
    for report in reports:
        for n in range(0, len(report) - 1):
            bits[n] += int(report[n])

    gamma = ''
    epsilon = ''

    for bit in bits:
        if bit > len(reports) / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2), int(epsilon, 2)


def main():
    with open('input1') as f:
        reports = f.readlines()

    gamma, epsilon = parse(reports)

    consumption = gamma * epsilon
    print(consumption)


if __name__ == '__main__':
    main()
