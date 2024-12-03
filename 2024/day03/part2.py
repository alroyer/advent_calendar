import re

with open('input1.txt') as f:
    data = f.read()

reg_do = re.compile(r'do\(\)')
reg_dont = re.compile(r"don't\(\)")

reg_mul = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

sum = 0

do = True

index_do = []
for match in reg_do.finditer(data):
    index_do.append(match.span()[0])

index_dont = []
for match in reg_dont.finditer(data):
    index_dont.append(match.span()[0])

for match in reg_mul.finditer(data):
    index = match.span()[0]

    if (index_do and index > index_do[0]) or (index_dont and index > index_dont[0]):
        if index_do and index_dont:
            do = index_do[0] < index_dont[0]
        elif index_do:
            do = True
        elif index_dont:
            do = False

        if do:
            index_do = index_do[1:]
        else:
            index_dont = index_dont[1:]

    if do:
        sum += int(match.group(1)) * int(match.group(2))

print(sum)
