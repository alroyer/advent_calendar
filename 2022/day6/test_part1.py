def find_marker(datastream: str) -> int:
    for index in range(0, len(datastream) - 3):
        characters = datastream[index:index + 4]

        found_duplicated = False
        for c in characters:
            if characters.count(c) > 1:
                found_duplicated = True
                break

        if not found_duplicated:
            return index + 4

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
    datastream = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
    assert find_marker(datastream) == 5


def test_datastream2():
    datastream = 'nppdvjthqldpwncqszvftbrmjlhg'
    assert find_marker(datastream) == 6


def test_datastream3():
    datastream = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
    assert find_marker(datastream) == 10


def test_datastream4():
    datastream = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
    assert find_marker(datastream) == 11
