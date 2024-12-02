network = {}

with open('input4.txt', 'r') as f:
    instructions, nodes = f.read().split('\n\n')
    for node in nodes.split('\n'):
        a, b = node.split(' = ')
        network[a] = (b[1:4], b[6:9])

nodes = []
for node in network.keys():
    if node.endswith('A'):
        nodes.append(node)

index = 0
while any(node for node in nodes if not node.endswith('Z')):
    instruction = instructions[index % len(instructions)]
    nodes = [network[node][0] if instruction == 'L' else network[node][1] for node in nodes]
    index += 1
print(index)
