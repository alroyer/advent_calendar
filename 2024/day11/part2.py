import math

with open('input1.txt') as f:
    data = f.read()

stones = list(map(int, data.replace('\n', '').split()))

blink = 75

for n in range(blink):
    print(f'{n}/{blink} - {len(stones)}')
    new_stones = []
    for index, stone in enumerate(stones):
        if stone == 0:
            new_stones.append(1)
            continue
        digits = int(math.log10(stone)) + 1
        if digits % 2 == 0:
            half = 10 ** (digits // 2)
            s1 = stone // half
            s2 = stone % half
            new_stones.append(int(s1))
            new_stones.append(int(s2))
        else:
            new_stones.append(stone * 2024)
    stones = new_stones

print(len(stones))
