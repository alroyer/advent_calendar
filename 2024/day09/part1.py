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
for free_index, n in enumerate(disk_map):
    if free_index % 2 == 0:
        blocks.append((n, id))
        id += 1
    elif n > 0:
        blocks.append((n, '.'))

free_index = next_free_index(blocks)
while free_index != -1:
    block_count, id = blocks.pop()
    free_space_count, _ = blocks[free_index]
    if free_space_count == block_count:
        blocks[free_index] = (block_count, id)
    elif free_space_count > block_count:
        del blocks[free_index]
        blocks.insert(free_index, (free_space_count - block_count, '.'))
        blocks.insert(free_index, (block_count, id))
    else:
        blocks[free_index] = (free_space_count, id)
        blocks.append((block_count - free_space_count, id))
    free_index = next_free_index(blocks)

disk = []
for block in blocks:
    if block[1] != '.':
        for n in range(block[0]):
            disk.append(block[1])

total = 0
for index, id in enumerate(disk):
    total += index * id

print(total)
