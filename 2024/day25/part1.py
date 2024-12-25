def lock_height(schema):
    heights = []
    for col in range(5):
        height = 0
        for row in range(1, 7):
            if schema[row][col] == '#':
                height += 1
        heights.append(height)
    return heights


def key_height(schema):
    heights = []
    for col in range(5):
        height = 0
        for row in range(5, -1, -1):
            if schema[row][col] == '#':
                height += 1
        heights.append(height)
    return heights


with open('input1.txt') as f:
    data = f.read().splitlines()

keys = []
locks = []

for index in range(0, len(data), 8):
    if data[index] == '#####':
        locks.append(*[data[index : index + 7]])
    else:
        keys.append(*[data[index : index + 7]])

keys_heights = [key_height(key) for key in keys]
locks_heights = [lock_height(lock) for lock in locks]

fit_count = 0
for key in keys_heights:
    for lock in locks_heights:
        fit = True
        for i in range(5):
            if key[i] + lock[i] > 5:
                fit = False
                break
        if fit:
            fit_count += 1
print(fit_count)
