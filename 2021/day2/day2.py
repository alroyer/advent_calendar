def main():
    with open('input1', 'r') as f:
        commands = f.readlines()

    hori = 0
    depth = 0
    aim = 0

    for command in commands:
        command, unit = command.split()
        unit = int(unit)

        if command == 'forward':
            hori += unit
            depth += (aim * unit)
        elif command == 'up':
            aim -= unit
        elif command == 'down':
            aim += unit

    print(hori * depth)


if __name__ == '__main__':
    main()
