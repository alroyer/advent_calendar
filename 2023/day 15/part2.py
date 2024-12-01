with open('input0.txt') as f:
    sequences = f.read().split(',')


def hash(string):
    current_value = 0
    for c in string:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


# sequences = ['rn=1', 'cm-', 'qp=3', 'cm=2', 'qp-', 'pc=4', 'ot=9', 'ab=5', 'pc-', 'pc=6', 'ot=7']

boxes = {}
for sequence in sequences:
    operation = '=' if '=' in sequence else '-'
    lens, focal_length = sequence.split(operation)
    box = hash(lens)

    if not box in boxes:
        boxes[box] = []

    if operation == '-':
        for index, item in enumerate(boxes[box]):
            if item[0] == lens:
                del boxes[box][index]
                break

    else:
        found = False
        for index, item in enumerate(boxes[box]):
            if item[0] == lens:
                boxes[box][index] = (lens, focal_length)
                found = True
                break
        if not found:
            boxes[box].append((lens, focal_length))

sum = 0
for key, values in boxes.items():
    for index, item in enumerate(values):
        sum += (index + 1) * (key + 1) * int(item[1])
print(sum)
