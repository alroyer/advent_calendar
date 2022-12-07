filesystem = {}


def read_data():
    with open('./2022/day7/input1.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]


def main():
    outputs = read_data()

    current_directory = ''

    for output in outputs:
        if output == '$ cd ..':
            current_directory = '.'.join(current_directory.split('.')[:-1])
        elif output.startswith('$ cd'):
            current_directory += '.' + output[5:]
            filesystem[current_directory] = []
        elif output.startswith('dir'):
            filesystem[current_directory + '.' + output[4:]] = []
        elif output.startswith('$ ls'):
            pass
        else:
            size, filename = output.split()
            filesystem[current_directory].append((filename, int(size)))

    sum = {}
    for directory, files in filesystem.items():
        sum[directory] = 0
        for filename, size in files:
            sum[directory] += size

    directories = list(sum.keys())
    directories.reverse()

    for directory in directories:
        parent_directory = '.'.join(directory.split('.')[:-1])
        if parent_directory in sum:
            sum[parent_directory] += sum[directory]

    total = 0
    for _, size in sum.items():
        if size <= 100000:
            total += size
    print(total)


if __name__ == '__main__':
    main()
