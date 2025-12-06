# problems = [
#     "123 328  51 64 ",
#     " 45 64  387 23 ",
#     "  6 98  215 314",
#     "*   +   *   +  ",
# ]

with open("input1.txt") as f:
    problems = f.readlines()

rows = len(problems)
cols = len(problems[0])

operations = problems[rows - 1].split()
index = 0

numbers = []
grand_toltal = 0
for col in range(cols):
    number = ""
    for row in range(rows - 1):
        number += problems[row][col]
    if number.strip():
        numbers.append(number)
    else:
        grand_toltal += eval(operations[index].join(numbers))
        numbers.clear()
        index += 1
# grand_toltal += eval(operations[-1].join(numbers))
print(grand_toltal)
