def read_data():
    with open('./2022/day4/input1.txt', 'r') as file:
        lines = file.readlines()
        return [line.strip().split(',') for line in lines]


def is_overlapped(section1, section2):
    s1v1, s1v2 = [int(x) for x in section1.split('-')]
    s2v1, s2v2 = [int(x) for x in section2.split('-')]

    if s1v1 >= s2v1 and s1v1 <= s2v2:
        return True
    if s1v2 >= s2v1 and s1v2 <= s2v2:
        return True

    if s2v1 >= s1v1 and s2v1 <= s1v2:
        return True
    if s2v2 >= s1v1 and s2v2 <= s1v2:
        return True

    return False


def main():
    sections = read_data()

    sum = 0
    for section1, section2 in sections:
        if is_overlapped(section1, section2):
            sum += 1
    print(sum)


if __name__ == '__main__':
    main()
