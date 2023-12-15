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

sum = 0
for sequence in sequences:
    sum += hash(sequence)
print(sum)
