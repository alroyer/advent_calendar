# rotations = [
#     "L68",
#     "L30",
#     "R48",
#     "L5",
#     "R60",
#     "L55",
#     "L1",
#     "L99",
#     "R14",
#     "L82",
# ]

# rotations = ["R1000"]

with open("input1.txt") as file:
    rotations = file.readlines()

count = 0
dial_pos = 50

print(f"The dial starts by pointing at {dial_pos}.")
for rotation in rotations:
    point_at_zero = 0

    dir = rotation[0]
    dist = int(rotation[1:])

    start = dial_pos

    point_at_zero += dist // 100
    dist %= 100

    match dir:
        case "L":
            dial_pos -= dist
        case _:
            dial_pos += dist

    dial_pos %= 100

    print(f"The dial is rotated {rotation} to point at {dial_pos}", end="")

    if dial_pos == 0:
        count += 1
        print(".")
    elif start == 0:
        print(".")
    elif dir == "L" and dial_pos > start:
        point_at_zero += 1
        print(f"; during this rotation, it\npoint at zero {point_at_zero}")
    elif dir == "R" and dial_pos < start:
        point_at_zero += 1
        print(f"; during this rotation, it\npoint at zero {point_at_zero}")
    else:
        print(".")

    count += point_at_zero

print(count)
