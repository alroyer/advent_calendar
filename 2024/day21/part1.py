from collections import deque

# codes = [
#     '869A',
#     '170A',
#     '319A',
#     '349A',
#     '489A',
# ]

codes = [
    '029A',
    '980A',
    '179A',
    '456A',
    '379A',
]


numpad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A'],
]

movepad = [
    [None, '^', 'A'],
    ['<', 'v', '>'],
]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(start, end, pad):
    queue = deque([(start, [])])
    visited = set()
    visited.add(start)
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path + [(x, y)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(pad) and 0 <= ny < len(pad[0]) and pad[nx][ny] is not None and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(x, y)]))
    return None


def find_position(key, pad):
    for i, row in enumerate(pad):
        for j, val in enumerate(row):
            if val == key:
                return (i, j)
    return None


def shortest_path(start_key, end_key, pad):
    start_pos = find_position(start_key, pad)
    end_pos = find_position(end_key, pad)
    return bfs(start_pos, end_pos, pad)


def convert_path(path):
    converted_path = ''
    for p in range(len(path) - 1):
        x1, y1 = path[p]
        x2, y2 = path[p + 1]
        if x1 == x2:
            if y1 < y2:
                converted_path += '>'
            else:
                converted_path += '<'
        else:
            if x1 < x2:
                converted_path += 'v'
            else:
                converted_path += '^'
    return converted_path


def solve(string, pad):
    string = 'A' + string
    path = ''
    for i in range(len(string) - 1):
        start = string[i]
        end = string[i + 1]
        p = shortest_path(start, end, pad)
        path += ''.join(convert_path(p)) + 'A'
    return path


complexity = 0

r = []

for code in codes:
    p1 = solve(code, numpad)
    p2 = solve(p1, movepad)
    p3 = solve(p2, movepad)

    r.append(f'{len(p3)} * {int(''.join([d for d in code if d.isdigit()]))}')

    complexity += len(p3) * int(''.join([d for d in code if d.isdigit()]))

    print(p3)
    print(p2)
    print(p1)
    print(code)

print(', '.join([str(x) for x in r]))
print(complexity)
