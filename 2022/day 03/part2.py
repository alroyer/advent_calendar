def read_data():
    with open('./2022/day3/input1.txt', 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


def priority(item):
    if item >= 'a' and item <= 'z':
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


def main():
    rucksacks = read_data()

    sum = 0

    for index in range(0, len(rucksacks), 3):
        rucksack1 = rucksacks[index]
        rucksack2 = rucksacks[index + 1]
        rucksack3 = rucksacks[index + 2]

        for item in rucksack1:
            if item in rucksack2 and item in rucksack3:
                sum += priority(item)
                break

    print(sum)


if __name__ == '__main__':
    main()
