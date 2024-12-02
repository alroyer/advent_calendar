from dataclasses import dataclass


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int


@dataclass
class Rule:
    category: str | None = None
    value: int | None = None
    operation: str | None = None
    destination: str | None = None


with open('input1.txt') as f:
    ws, ps = f.read().split('\n\n')

worflows = {}
for w in ws.split():
    name, rs = w.split('{')
    worflows[name] = []
    for r in rs[:-1].split(','):
        if ':' in r:
            o, d = r.split(':')
            category, operation, value = o[0], o[1], o[2:]
            if not operation in '<>':
                assert False
            destination = d
            worflows[name].append(
                Rule(category=category, value=int(value), operation=operation, destination=destination)
            )
        else:
            worflows[name].append(Rule(destination=r))

parts = []
for p in ps.split():
    x, m, a, s = p[1:-1].split(',')
    parts.append(Part(int(x[2:]), int(m[2:]), int(a[2:]), int(s[2:])))

sum = 0
for part in parts:
    destination = 'in'
    while not destination in ['R', 'A']:
        print(f'{destination} ', end='')
        rules = worflows[destination]
        for rule in rules:
            apply = False
            if not rule.category:
                destination = rule.destination
            elif rule.category == 'x':
                if rule.operation == '>' and part.x > rule.value:
                    apply = True
                elif rule.operation == '<' and part.x < rule.value:
                    apply = True
            elif rule.category == 'm':
                if rule.operation == '>' and part.m > rule.value:
                    apply = True
                elif rule.operation == '<' and part.m < rule.value:
                    apply = True
            elif rule.category == 'a':
                if rule.operation == '>' and part.a > rule.value:
                    apply = True
                elif rule.operation == '<' and part.a < rule.value:
                    apply = True
            elif rule.category == 's':
                if rule.operation == '>' and part.s > rule.value:
                    apply = True
                elif rule.operation == '<' and part.s < rule.value:
                    apply = True
            if apply:
                destination = rule.destination
                break
    if destination == 'A':
        sum += part.x + part.m + part.a + part.s
    print(destination)
print(sum)
