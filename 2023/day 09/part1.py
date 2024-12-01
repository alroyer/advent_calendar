histories = []
with open('input1.txt', 'r') as f:
    data = f.read().split('\n')
    for history in data:
        histories.append([int(n) for n in history.split(' ')])

sum = 0

for history in histories:
    diffs = history.copy()
    all_diffs = [diffs]
    while any(diffs):
        new_diffs = []
        for n in range(len(diffs) - 1):
            new_diffs.append(diffs[n + 1] - diffs[n])
        diffs = new_diffs
        all_diffs.append(diffs)
    all_diffs[-1].append(0)

    for n in range(len(all_diffs) - 2, -1, -1):
        all_diffs[n].append(all_diffs[n][-1] + all_diffs[n + 1][-1])

    sum = sum + all_diffs[0][-1]

print(sum)
