def horizontal(pattern):
    for col in range(len(pattern[0]) - 1):
        col1 = col
        col2 = col + 1
        pairs = [(col1, col2)]
        while col1 > 0 and col2 < (len(pattern[0]) - 1):
            col1 -= 1
            col2 += 1
            pairs.append((col1, col2))
        reflexion = True
        diff = 0
        for pair in pairs:
            p1 = [pattern[n][pair[0]] for n in range(len(pattern))]
            p2 = [pattern[n][pair[1]] for n in range(len(pattern))]
            reflexion = p1 == p2
            if not reflexion:
                for n in range(len(p1)):
                    if p1[n] != p2[n]:
                        diff += 1
                    if diff >= 2:
                        reflexion = False
                        break
        if diff == 1:
            return col + 1
    return None


def vertical(pattern):
    for row in range(len(pattern) - 1):
        row1 = row
        row2 = row + 1
        pairs = [(row1, row2)]
        while row1 > 0 and row2 < (len(pattern) - 1):
            row1 -= 1
            row2 += 1
            pairs.append((row1, row2))
        reflexion = True
        diff = 0
        for pair in pairs:
            p1 = pattern[pair[0]]
            p2 = pattern[pair[1]]
            reflexion = p1 == p2
            if not reflexion:
                for n in range(len(p1)):
                    if p1[n] != p2[n]:
                        diff += 1
                    if diff >= 2:
                        reflexion = False
                        break
        if diff == 1:
            return row + 1
    return None


patterns = []
with open('input0.txt', 'r') as f:
    for p in f.read().split('\n\n'):
        patterns.append(p.split())

sum = 0
for pattern in patterns:
    col = horizontal(pattern)
    if col:
        sum += col
    else:
        col = vertical(pattern)
        if col:
            sum += 100 * col
        else:
            assert False
print(sum)
