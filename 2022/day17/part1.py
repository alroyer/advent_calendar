rock1 = """@@@@"""
rock2 = """.@.
@@@
.@."""
rock3 = """..@
..@
@@@"""
rock4 = """@
@
@
@"""
rock5 = """@@
@@"""

rocks = [rock1, rock2, rock3, rock4, rock5]
rock_index = 0

width = 7
# appears 2 to the left and three above the hightest or the floor

cave = [
    '+-------+',
    '|.......|',
    '|.......|',
    '|.......|',
]


def read_data():
    with open('./2022/day17/input0.txt', 'r') as file:
        return list(file.readline().strip())


streams = read_data()
stream_index = 0


def get_next_rock():
    global rock_index
    rock = rocks[rock_index % len(rocks)]
    rock_index += 1
    return rock


def get_next_stream():
    global stream_index
    stream = streams[stream_index % len(streams)]
    stream_index += 1
    return stream


def print_cave():
    for i in range(len(cave) - 1, -1, -1):
        print(cave[i])


def new_rock_begin_falling():
    rock = get_next_rock()

    blank_count = 0
    for i in range(len(cave) - 1, 0, -1):
        if '#' in cave[i]:
            break
        blank_count += 1

    need_blank = (3 + len(rock.split())) - blank_count
    for _ in range(need_blank):
        cave.append('|.......|')

    cave_index = len(cave) - 1
    for index, line in enumerate(rock.split('\n')):
        x = cave[cave_index - index][:3] + line
        cave[cave_index - index] = x + '.' * (8 - len(x)) + '|'


def check_done_falling():
    for i in range(1, len(cave)):
        l1 = cave[i]
        l2 = cave[i - 1]
        for j in range(1, width + 1):
            if l1[j] == '@' and (l2[j] == '#' or l2[j] == '-'):
                return True
    return False


def mark_falling_rock():
    for index in range(len(cave)):
        cave[index] = cave[index].replace('@', '#')


def rock_fall():
    can_fall = True
    for i in range(1, len(cave)):
        if '@' in cave[i]:
            for j in range(len(cave[i])):
                if cave[i][j] == '@' and (cave[i - 1][j] == '-' or cave[i - 1][j] == '#'):
                    can_fall = False

    if can_fall:
        for i in range(2, len(cave)):
            l1 = cave[i]
            l2 = cave[i - 1]
            for j in range(1, width + 1):
                if l1[j] == '@' and l2[j] == '.':
                    l2 = l2[:j] + '@' + l2[j+1:]
                    l1 = l1[:j] + '.' + l1[j+1:]
                    cave[i] = l1
                    cave[i - 1] = l2


def push_rock():
    stream = get_next_stream()

    rock_height = 0
    can_push_height = 0

    for line in cave:
        if '@' in line:
            rock_height += 1
        if stream == '<' and '.@' in line:
            can_push_height += 1
        elif stream == '>' and '@.' in line:
            can_push_height += 1

    if rock_height == can_push_height:
        for index, line in enumerate(cave):
            if stream == '<' and '.@' in line:
                begin = line.find('@')
                end = line.rfind('@')

                x = line[:begin - 1]
                y = line[end + 1:]
                z = line[begin:end + 1]

                cave[index] = x + z + '.' + y

            elif stream == '>' and '@.' in line:
                begin = line.find('@')
                end = line.rfind('@')

                x = line[:begin]
                y = line[end + 2:]
                z = line[begin:end + 1]

                cave[index] = x + '.' + z + y


def main():
    for _ in range(5):
        new_rock_begin_falling()

        print()
        print_cave()

        while not check_done_falling():
            push_rock()
            rock_fall()
        push_rock()
        rock_fall()
        mark_falling_rock()

        print()
        print_cave()

    # print_cave()


if __name__ == '__main__':
    main()
