def format(record):
    conditions, groups = record.split(' ')
    return conditions, [int(n) for n in groups.split(',')]


def is_valid(conditions, groups):
    in_group = False
    found_groups = []
    count = 0
    for condition in conditions:
        if condition == '.':
            if in_group:
                in_group = False
                found_groups.append(count)
                count = 0
        elif condition == '#':
            in_group = True
            count += 1
    if in_group:
        found_groups.append(count)
    return groups == found_groups


def arrange(conditions, a):
    for index, condition in enumerate(conditions):
        if condition == '?':
            new_condition, a = a[0], a[1:]
            if new_condition == '1':
                conditions = conditions[:index] + '#' + conditions[index + 1 :]
            else:
                conditions = conditions[:index] + '.' + conditions[index + 1 :]
            if not a:
                break
    return conditions


def count_arrangements(conditions, groups):
    count = 0
    unknown = conditions.count('?')
    for n in range(1, 2**unknown):
        new_conditions = arrange(conditions, f'{bin(n)[2:]:>0{unknown}}')
        if is_valid(new_conditions, groups):
            count = count + 1
    return count


with open('input2.txt', 'r') as f:
    records = f.read().split('\n')

sum = 0
for record in records:
    conditions, groups = format(record)
    sum = sum + count_arrangements(conditions, groups)
print(sum)
