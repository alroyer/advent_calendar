with open('input1.txt') as f:
    data = f.read()

rules = []
updates = []

for line in data.split():
    if '|' in line:
        rules.append(line.split('|'))
    elif ',' in line:
        updates.append(line.split(','))

total = 0

for update in updates:
    index = {}
    for number, page in enumerate(update):
        index[page] = number

    correct = True

    for n1, n2 in rules:
        i1 = index.get(n1)
        i2 = index.get(n2)

        if i1 is None or i2 is None:
            continue

        if i1 > i2:
            correct = False
            break

    if correct:
        total += int(update[len(update) // 2])

print(total)
