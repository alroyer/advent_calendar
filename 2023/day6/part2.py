from functools import reduce


def main() -> None:
    max_time = 38947970
    record_distance = 241154910741091

    count = 0
    for t in range(max_time + 1):
        d = (max_time - t) * t
        if d > record_distance:
            count += 1
        if count > 0 and d <= record_distance:
            break
    print(count)


if __name__ == '__main__':
    main()
