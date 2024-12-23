from collections import defaultdict


def read_connections(file_path):
    connections = defaultdict(set)
    with open(file_path, 'r') as file:
        for line in file:
            a, b = line.strip().split('-')
            connections[a].add(b)
            connections[b].add(a)
    return connections


def find_triplets(connections):
    triplets = set()
    for node in connections:
        for neighbor in connections[node]:
            for second_neighbor in connections[neighbor]:
                if second_neighbor in connections[node] and node != second_neighbor:
                    triplet = tuple(sorted([node, neighbor, second_neighbor]))
                    triplets.add(triplet)
    return triplets


connections = read_connections('input1.txt')
triplets = find_triplets(connections)

count = 0
for triplet in triplets:
    if any(s.startswith('t') for s in triplet):
        count += 1
print(count)
