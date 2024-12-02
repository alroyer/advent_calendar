with open('input1.txt') as f:
    data = f.read()

l1 = []
l2 = []

for index, value in enumerate(data.split()):
    l1.append(int(value)) if index % 2 else l2.append(int(value))

l1.sort()
l2.sort()

sum = 0

for index in range(len(l1)):
    sum += abs(l1[index] - l2[index])

print(sum)
