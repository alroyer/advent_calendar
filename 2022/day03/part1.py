def read_data():
    rucksacks = []
    with open('./2022/day3/input1.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            rucksack = line.strip()
            lenght = int(len(rucksack) / 2)
            rucksacks.append((rucksack[:lenght], rucksack[lenght:]))
    return rucksacks


def priority(item):
    if item >= 'a' and item <= 'z':
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


def main():
    rucksacks = read_data()

    sum = 0
    for rucksack in rucksacks:
        for item in rucksack[0]:
            if item in rucksack[1]:
                sum += priority(item)
                break
    print(sum)


if __name__ == '__main__':
    main()
