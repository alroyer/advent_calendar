def push(stream, cave):
    for index, line in enumerate(cave):
        if stream == '<' and '.@' in line:
            begin = line.find('@')
            end = line.rfind('@')

            x = line[:begin - 1]
            y = line[end + 1:]
            z = line[begin:end + 1]

            cave[index] = x + z + '.' + y
            pass

        elif stream == '>' and '@.' in line:
            begin = line.find('@')
            end = line.rfind('@')

            x = line[:begin]
            y = line[end + 2:]
            z = line[begin:end + 1]

            cave[index] = x + '.' + z + y
            pass

    return cave


def test_push_left0():
    cave = [
        '|.......|',
        '|@@@@...|',
        '|.......|',
        '|.......|',
        '+-------+',
    ]

    expected_cave = [
        '|.......|',
        '|@@@@...|',
        '|.......|',
        '|.......|',
        '+-------+',
    ]

    result = push('<', cave)

    assert result == expected_cave


def test_push_left1():
    cave = [
        '|.......|',
        '|..@@@@.|',
        '|.......|',
        '|.......|',
        '+-------+',
    ]

    expected_cave = [
        '|.......|',
        '|.@@@@..|',
        '|.......|',
        '|.......|',
        '+-------+',
    ]

    result = push('<', cave)

    assert result == expected_cave


def test_push_left2():
    cave = [
        '|.......|',
        '|#.@@@@.|',
        '|.......|',
        '|.......|',
        '+-------+',
    ]

    expected_cave = [
        '|.......|',
        '|#@@@@..|',
        '|.......|',
        '|.......|',
        '+-------+',
    ]

    result = push('<', cave)

    assert result == expected_cave


def test_push_right0():
    cave = [
        '|.......|',
        '|...@@@@|',
        '|.......|',
        '|.......|',
        '+-------+',
    ]

    expected_cave = [
        '|.......|',
        '|...@@@@|',
        '|.......|',
        '|.......|',
        '+-------+',
    ]

    result = push('>', cave)

    assert result == expected_cave


def test_push_right1():
    cave = [
        '|.......|',
        '|..@@@@.|',
        '|.......|',
        '|.......|',
        '+-------+',
    ]

    expected_cave = [
        '|.......|',
        '|...@@@@|',
        '|.......|',
        '|.......|',
        '+-------+',
    ]

    result = push('>', cave)

    assert result == expected_cave


def test_push_right2():
    cave = [
        '|.......|',
        '|.@@@@.#|',
        '|.......|',
        '|.......|',
        '+-------+',
    ]

    expected_cave = [
        '|.......|',
        '|..@@@@#|',
        '|.......|',
        '|.......|',
        '+-------+',
    ]

    result = push('>', cave)

    assert result == expected_cave
