network = {}

with open('input2.txt', 'r') as f:
    instructions, nodes = f.read().split('\n\n')
    for node in nodes.split('\n'):
        a, b = node.split(' = ')
        network[a] = (b[1:4], b[6:9])

node = 'AAA'
index = 0
while node != 'ZZZ':
    instruction = instructions[index % len(instructions)]
    node = network[node][0] if instruction == 'L' else network[node][1]
    index += 1
print(index)
