with open('input1.txt') as f:
    data = f.read()

stones = list(data.replace('\n', '').split())

blink = 25

for _ in range(blink):
    new_stones = []
    for index, stone in enumerate(stones):
        digits = len(stone)
        if stone == '0':
            new_stones.append('1')
        elif digits % 2 == 0:
            s1 = stone[: digits // 2]
            s2 = stone[digits // 2 :]
            new_stones.append(f'{int(s1)}')
            new_stones.append(f'{int(s2)}')
        else:
            new_stones.append(str(int(stone) * 2024))
    stones = new_stones
    # print(' '.join(stones))

print(len(stones))
