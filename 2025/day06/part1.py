# problems = [
#     "123 328  51  64",
#     " 45  64 387  23",
#     "  6  98 215 314",
#     "*   +   *   +",
# ]

with open("input1.txt") as f:
    problems = f.readlines()

parsed_problems = []
for data in problems:
    parsed_problems.append(data.split())

rows = len(parsed_problems)
cols = len(parsed_problems[0])

grand_total = 0
for col in range(cols):
    numbers = []
    for row in range(rows - 1):
        numbers.append(parsed_problems[row][col])
    grand_total += eval(parsed_problems[rows - 1][col].join(numbers))
print(grand_total)
