from moves import movepad, numpad

codes = [
    # '029A',
    # '980A',
    # '179A',
    # '456A',
    '379A',
]


def solve(string, pad):
    string = 'A' + string
    path = ''
    for i in range(len(string) - 1):
        start = string[i]
        end = string[i + 1]
        if start == end:
            path += 'A'
        else:
            path += pad[(start, end)] + 'A'
    return path


complexity = 0

for code in codes:
    path = solve(code, numpad)
    print(path)

    path = solve(path, movepad)
    print(path)

    path = solve(path, movepad)
    print(path)

    complexity += len(path) * int(''.join([d for d in code if d.isdigit()]))
print(complexity)
