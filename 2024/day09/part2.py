from dataclasses import dataclass


def print_disk(blocks):
    for block in blocks:
        print('.' * block.size if block.free else f'{block.id}' * block.size, end='')
    print()


def next_file(blocks, index=None):
    if index is None:
        index = len(blocks) - 1
    for i in range(index, 0, -1):
        if not blocks[i].free:
            return i, blocks[i]
    return -1, None


def next_free(blocks, size, index=None):
    index = index if index is not None else 0
    for i in range(index, len(blocks) - 1):
        if blocks[i].free and blocks[i].size >= size:
            return i, blocks[i]
    return -1, None


@dataclass(frozen=True)
class Block:
    id: int
    size: int
    free: bool = False


with open('input1.txt') as f:
    data = f.read()

disk_map = list(map(int, data.replace('\n', '')))

blocks = []
id = 0
for index, size in enumerate(disk_map):
    if index % 2 == 0:
        blocks.append(Block(id, size))
        id += 1
    elif size > 0:
        blocks.append(Block(-1, size, free=True))

file_index, file_block = next_file(blocks)
while file_block:
    free_index, free_block = next_free(blocks, file_block.size)
    if free_block and free_index < file_index:
        del blocks[file_index]
        if free_block.size == file_block.size:
            blocks[free_index] = file_block
            blocks.insert(file_index, Block(-1, file_block.size, free=True))
        elif free_block.size > file_block.size:
            blocks[free_index] = file_block
            blocks.insert(free_index + 1, Block(-1, free_block.size - file_block.size, free=True))
            blocks.insert(file_index + 1, Block(-1, file_block.size, free=True))
        file_index, file_block = next_file(blocks, file_index)
    else:
        file_index, file_block = next_file(blocks, file_index - 1)
    # print_disk(blocks)

total = 0
index = 0
for block in blocks:
    for n in range(block.size):
        if not block.free:
            total += index * block.id
        index += 1

print(total)
