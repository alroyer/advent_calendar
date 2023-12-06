from functools import reduce


def read_data(path: str) -> list[str]:
    with open(path, 'r') as f:
        data = f.readlines()
        return [d.strip() for d in data]


def main() -> None:
    data = read_data('input1.txt')

    time = [int(n) for n in filter(None, data[0].split(':')[1].split(' '))]
    distance = [int(n) for n in filter(None, data[1].split(':')[1].split(' '))]

    total = []
    for n in range(len(time)):
        max_time = time[n]
        record_distance = distance[n]
        count = 0
        for t in range(max_time + 1):
            d = (max_time - t) * t
            if d > record_distance:
                count += 1
        total.append(count)
    print(reduce(lambda a, b: a * b, total))


if __name__ == '__main__':
    main()
