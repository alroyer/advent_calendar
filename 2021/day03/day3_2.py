def parse(reports):
    ori = reports

    for index in range(len(reports[0]) - 1):
        c = count(index, reports)
        keep_one = c >= len(reports) / 2
        reports = [report for report in reports if keep_one and report[index]
                   == '1' or not keep_one and report[index] == '0']
        if len(reports) == 1:
            break

    oxygen = int(reports[0], 2)
    print(oxygen)

    for index in range(len(ori[0]) - 1):
        c = count(index, ori)
        keep_one = c < len(ori) / 2
        ori = [report for report in ori if keep_one and report[index]
               == '1' or not keep_one and report[index] == '0']
        if len(ori) == 1:
            break

    co2 = int(ori[0], 2)
    print(co2)

    print(oxygen * co2)


def count(index, reports):
    count = 0
    for report in reports:
        count += int(report[index])
    return count


def main():
    with open('input1') as f:
        reports = f.readlines()

    parse(reports)


if __name__ == '__main__':
    main()
