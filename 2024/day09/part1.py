def next_free_index(blocks):
    for index, block in enumerate(blocks):
        if block[1] == '.' and index < len(blocks) - 1:
            return index
    return -1


with open('input1.txt') as f:
    data = f.read()

disk_map = list(map(int, data.replace('\n', '')))

blocks = []
id = 0
for index, n in enumerate(disk_map):
    if index % 2 == 0:
        blocks.append((n, id))
        id += 1
    elif n > 0:
        blocks.append((n, '.'))

index = next_free_index(blocks)
while index != -1:
    block_count, id = blocks.pop()
    free_space_count, _ = blocks[index]
    if free_space_count == block_count:
        blocks[index] = (block_count, id)
    elif free_space_count > block_count:
        del blocks[index]
        blocks.insert(index, (free_space_count - block_count, '.'))
        blocks.insert(index, (block_count, id))
    else:
        blocks[index] = (free_space_count, id)
        blocks.append((block_count - free_space_count, id))
    index = next_free_index(blocks)

disk = []
for block in blocks:
    if block[1] != '.':
        for n in range(block[0]):
            disk.append(block[1])

total = 0
for index, id in enumerate(disk):
    total += index * id

print(total)
