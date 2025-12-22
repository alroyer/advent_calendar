from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


with open("input1.txt") as f:
    tiles = []
    for line in f:
        x, y = map(int, line.strip().split(","))
        tiles.append(Point(x, y))

# tiles = [
#     Point(7, 1),
#     Point(11, 1),
#     Point(11, 7),
#     Point(9, 7),
#     Point(9, 5),
#     Point(2, 5),
#     Point(2, 3),
#     Point(7, 3),
# ]

largest_area = None
for t1 in tiles:
    for t2 in tiles:
        if t1 == t2:
            continue
        area = (abs(t2.x - t1.x) + 1) * (abs(t2.y - t1.y) + 1)
        if largest_area is None or area > largest_area[0]:
            largest_area = (area, t1, t2)
print(largest_area)
