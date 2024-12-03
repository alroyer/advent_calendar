import re

with open('input1.txt') as f:
    data = f.read()

p = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
matchs = p.findall(data)

sum = 0

for match in matchs:
    sum += int(match[0]) * int(match[1])

print(sum)
