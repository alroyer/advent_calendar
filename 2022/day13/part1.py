def read_data():
    with open('./2022/day13/input1.txt', 'r') as file:
        packets = []
        read_left = True
        for line in file.readlines():
            if line == '\n':
                packets.append((left, right))
                read_left = True
            else:
                if read_left:
                    left = eval(line.strip())
                    read_left = False
                else:
                    right = eval(line.strip())
        packets.append((left, right))
        return packets


IN_RIGHT_ORDER = 0
SAME_INTEGER = 1
NOT_IN_RIGHT_ORDER = 2


def compare(left, right):
    if not left and right:
        return IN_RIGHT_ORDER
    elif left and not right:
        return NOT_IN_RIGHT_ORDER
    elif not left and not right:
        return SAME_INTEGER

    if type(left) == int and type(right) == int:
        if left < right:
            return IN_RIGHT_ORDER
        elif left == right:
            return SAME_INTEGER
        else:
            return NOT_IN_RIGHT_ORDER

    elif type(left) == list and type(right) == list:
        result = compare(left[0], right[0])
        if result == SAME_INTEGER:
            left = left[1:]
            right = right[1:]
            if not left and right:
                return IN_RIGHT_ORDER
            elif left and not right:
                return NOT_IN_RIGHT_ORDER
            elif not left and not right:
                return SAME_INTEGER

        while result == SAME_INTEGER:
            result = compare(left[0], right[0])
            if result == SAME_INTEGER:
                left = left[1:]
                right = right[1:]
                if not left and right:
                    return IN_RIGHT_ORDER
                elif left and not right:
                    return NOT_IN_RIGHT_ORDER
                elif not left and not right:
                    return SAME_INTEGER

        return result

    elif type(left) == int:
        return compare([left], right)
    elif type(right) == int:
        return compare(left, [right])


def main():
    packets = read_data()

    in_the_right_order = []
    for index, packet in enumerate(packets):
        if compare(packet[0], packet[1]) == IN_RIGHT_ORDER:
            in_the_right_order.append(index + 1)

    # print(in_the_right_order)

    print(sum(in_the_right_order))


if __name__ == '__main__':
    main()
