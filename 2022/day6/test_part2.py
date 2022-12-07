def find_marker(datastream: str) -> int:
    for index in range(0, len(datastream) - 13):
        characters = datastream[index:index + 14]

        found_duplicated = False
        for c in characters:
            if characters.count(c) > 1:
                found_duplicated = True
                break

        if not found_duplicated:
            return index + 14

    raise Exception()


def read_data() -> str:
    with open('./2022/day6/input0.txt', 'r') as file:
        return file.readline()


def main():
    datastream = read_data()
    print(find_marker(datastream))


if __name__ == '__main__':
    main()


def test_datastream1():
    datastream = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    assert find_marker(datastream) == 19


def test_datastream2():
    datastream = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
    assert find_marker(datastream) == 23


def test_datastream3():
    datastream = 'nppdvjthqldpwncqszvftbrmjlhg'
    assert find_marker(datastream) == 23


def test_datastream4():
    datastream = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
    assert find_marker(datastream) == 29


def test_datastream5():
    datastream = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
    assert find_marker(datastream) == 26
