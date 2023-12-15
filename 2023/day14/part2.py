with open('input0.txt') as f:
    data = f.read().split('\n')


def north(data):
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            for n, row in enumerate(data[j]):
                if row == 'O' and data[j - 1][n] == '.':
                    data[j - 1] = data[j - 1][:n] + 'O' + data[j - 1][n + 1 :]
                    data[j] = data[j][:n] + '.' + data[j][n + 1 :]


def west(data):
    for i in range(len(data)):
        for j in range(1, len(data[0])):
            for n in range(j, 0, -1):
                if data[i][n] == 'O' and data[i][n - 1] == '.':
                    data[i] = data[i][: n - 1] + 'O.' + data[i][n + 1 :]


def south(data):
    for i in range(len(data) - 2, -1, -1):
        for j in range(i, len(data) - 1):
            for n, row in enumerate(data[j]):
                if row == 'O' and data[j + 1][n] == '.':
                    data[j + 1] = data[j + 1][:n] + 'O' + data[j + 1][n + 1 :]
                    data[j] = data[j][:n] + '.' + data[j][n + 1 :]


def east(data):
    for i in range(len(data)):
        for j in range(len(data[0]) - 2, -1, -1):
            for n in range(j, len(data[0]) - 1):
                if data[i][n] == 'O' and data[i][n + 1] == '.':
                    data[i] = data[i][:n] + '.O' + data[i][n + 2 :]


def cycle(data):
    north(data)
    west(data)
    south(data)
    east(data)


for c in range(1000000000):
    cycle(data)
    if c % 10000 == 0:
        print(f'{c=}')

total_load = 0
for index, row in enumerate(data):
    total_load += row.count('O') * (len(data) - index)
print(total_load)
