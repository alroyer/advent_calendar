def main(filename):
    with open(filename, 'r') as file:
        items_calories = file.readlines()

        max_colories = []
        current_total_calories = 0

        for item_calories in items_calories:
            if item_calories == '\n':
                max_colories.append(current_total_calories)
                current_total_calories = 0
            else:
                current_total_calories = current_total_calories + \
                    int(item_calories)

        if current_total_calories != 0:
            max_colories.append(current_total_calories)

        max_colories.sort(reverse=True)

        print(sum(max_colories[:3]))


if __name__ == '__main__':
    main('2022/input1.txt')
