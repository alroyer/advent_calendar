def read_numbers(file):
    numbers = [int(number) for number in file.readline().split(',')]
    return numbers


def read_boards(file):
    lines = [line for line in file.readlines() if line.strip()]
    boards = []
    index = 0
    while index < len(lines):
        boards.append(create_board(lines[index: index + 5]))
        index += 5
    return boards


def create_board(lines):
    board = [0] * 5
    for index in range(5):
        board[index] = [(int(number), False)
                        for number in lines[index].split()]
    return board


def print_board(board):
    for row in range(5):
        for col in range(5):
            print(board[row][col], end=' ')
        print()
    print()


def look_for(number, boards):
    for board in boards:
        for row in range(5):
            for col in range(5):
                board[row][col] = (board[row][col][0],
                                   board[row][col][1] or board[row][col][0] == number)


def main():
    with open('input0', 'r') as file:
        numbers = read_numbers(file)
        boards = read_boards(file)

        # for board in boards:
        #     print_board(board)

    for number in numbers:
        look_for(number, boards)
        # look_for_winner(boards)

    for board in boards:
        print_board(board)


if __name__ == '__main__':
    main()
