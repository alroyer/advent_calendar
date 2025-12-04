with open("input1.txt") as file:
    rotations = file.readlines()

count = 0
dial_pos = 50

for rotation in rotations:
    dir = rotation[0]
    dist = int(rotation[1:])

    match dir:
        case "L":
            dial_pos -= dist
        case _:
            dial_pos += dist

    dial_pos %= 100

    if dial_pos == 0:
        count += 1

    print(f"The dial is rotated {rotation} to point at {dial_pos}.")

print(count)
