def main():
    with open('input1', 'r') as f:
        depths = f.readlines()
    depths = [int(depth) for depth in depths]

    count = 0
    for n in range(1, len(depths)):
        if depths[n] > depths[n-1]:
            count += 1

    print(f'COUNT: {count}')


if __name__ == '__main__':
    main()
