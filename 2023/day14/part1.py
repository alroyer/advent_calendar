with open('input1.txt') as f:
    data = f.read().split('\n')

for index in range(1, len(data)):
    for j in range(index, 0, -1):
        for n, row in enumerate(data[j]):
            if row == 'O' and data[j - 1][n] == '.':
                data[j - 1] = data[j - 1][:n] + 'O' + data[j - 1][n + 1 :]
                data[j] = data[j][:n] + '.' + data[j][n + 1 :]

total_load = 0
for index, row in enumerate(data):
    total_load += row.count('O') * (len(data) - index)
print(total_load)
