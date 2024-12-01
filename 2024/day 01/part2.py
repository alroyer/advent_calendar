with open('input1.txt') as f:
    data = f.read()

l1 = []
l2 = []

for index, value in enumerate(data.split()):
    l1.append(int(value)) if index % 2 else l2.append(int(value))

sum = 0

for value in l1:
    sum += value * l2.count(value)

print(sum)
