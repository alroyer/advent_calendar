import itertools


def compute_combinations(n, operations):
    return list(itertools.product(operations, repeat=n))


with open('input1.txt') as f:
    data = f.read()

equations = []

for d in filter(None, data.split('\n')):
    total, numbers = d.split(': ')
    equations.append((int(total), list(map(int, numbers.split()))))

available_operations = [
    'add',
    'mul',
]

total_calibration = 0

for equation in equations:
    test_value, numbers = equation
    all_operations = compute_combinations(len(numbers) - 1, available_operations)

    for operations in all_operations:
        total = numbers[0]
        index = 1
        for operation in operations:
            if operation == 'add':
                total += numbers[index]
            else:
                total *= numbers[index]
            index += 1
        if total == test_value:
            total_calibration += total
            break

print(total_calibration)
