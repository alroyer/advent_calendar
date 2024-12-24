with open('input2.txt') as f:
    data = f.read().splitlines()

wires = {}

operations = []

for d in data:
    if ':' in d:
        k, v = d.split(': ')
        wires[k] = int(v)
    elif '->' in d:
        wires_and_gates, out = d.split(' -> ')
        wires[out] = None

        in1, gate, in2 = wires_and_gates.split(' ')
        operations.append((in1, gate, in2, out))

        if in1 not in wires:
            wires[in1] = None

        if in2 not in wires:
            wires[in2] = None

index = 0
while operations:
    in1, gate, in2, out = operations[index]

    if wires[in1] is None or wires[in2] is None:
        index = (index + 1) % len(operations)
        continue

    if gate == 'AND':
        wires[out] = wires[in1] & wires[in2]
    elif gate == 'OR':
        wires[out] = wires[in1] | wires[in2]
    elif gate == 'XOR':
        wires[out] = wires[in1] ^ wires[in2]

    del operations[index]
    index = 0

bits = ''.join([str(wires[k]) for k in reversed(sorted(list(filter(lambda x: x.startswith('z'), wires.keys()))))])
decimal_number = int(bits, 2)

print(bits, decimal_number)
