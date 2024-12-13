r = 8400
a = 94
b = 22

solutions = []
for i in range(100):
    for j in range(100):
        if (a * i + b * j) == r:
            solutions.append((i, j, i + j))

x = min(solutions, key=lambda x: x[2])
print(x)
