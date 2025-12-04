# banks = [
#     "987654321111111",
#     "811111111111119",
#     "234234234234278",
#     "818181911112111",
# ]

with open("input1.txt") as f:
    banks = [line.strip() for line in f.readlines()]

total_joltage = 0
for batteries in banks:
    lb = (0, batteries[0])
    for index, battery in enumerate(batteries[:-1]):
        if battery > lb[1]:
            lb = (index, battery)
    rb = max(batteries[lb[0] + 1 :])
    total_joltage += int(f"{lb[1]}{rb}")
print(total_joltage)
