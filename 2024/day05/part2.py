with open('input1.txt') as f:
    data = f.read()


def is_correct(rules, update):
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

    return correct


def apply(rules, update):
    rules_to_apply = []

    for rule in rules:
        if rule[0] in update and rule[1] in update:
            rules_to_apply.append((int(rule[0]), int(rule[1])))

    graph = {}
    for rule in rules_to_apply:
        if rule[0] not in graph:
            graph[rule[0]] = []
        graph[rule[0]].append(rule[1])

    visited = set()
    stack = []

    def topological_sort(page):
        if page in visited:
            return
        visited.add(page)
        if page in graph:
            for next_page in graph[page]:
                topological_sort(next_page)
        stack.append(page)

    for page in graph:
        if page not in visited:
            topological_sort(page)

    stack.reverse()
    return stack


rules = []
updates = []

for line in data.split():
    if '|' in line:
        rules.append(line.split('|'))
    elif ',' in line:
        updates.append(line.split(','))

total = 0

for update in updates:
    if not is_correct(rules, update):
        fixed_update = apply(rules, update)
        total += fixed_update[len(fixed_update) // 2]

print(total)
