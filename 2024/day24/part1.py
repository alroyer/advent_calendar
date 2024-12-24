with open('input2.txt') as f:
    data = f.read().splitlines()

wires = {}

operations = []

for d in data:
    if ':' in d:
        k, v = d.split(': ')
        wires[k] = int(v)
    elif '->' in d:
        oper, output = d.split(' -> ')
        wires[output] = None

        input1, oper, input2 = oper.split(' ')
        operations.append((input1, oper, input2, output))

        if input1 not in wires:
            wires[input1] = None

        if input2 not in wires:
            wires[input2] = None

index = 0
while operations:
    input1, oper, input2, output = operations[index]
    if wires[input1] is None or wires[input2] is None:
        index += 1
        index %= len(operations)
        continue

    if oper == 'AND':
        wires[output] = wires[input1] & wires[input2]
    elif oper == 'OR':
        wires[output] = wires[input1] | wires[input2]
    elif oper == 'XOR':
        wires[output] = wires[input1] ^ wires[input2]
    del operations[index]
    index = 0

bits = ''.join([str(wires[k]) for k in reversed(sorted(list(filter(lambda x: x.startswith('z'), wires.keys()))))])
decimal_number = int(bits, 2)

print(bits, decimal_number)
