from dataclasses import dataclass


@dataclass
class Point:
    y: int
    x: int

    def __hash__(self) -> int:
        return hash((self.y, self.x))


# diagram = [
#     ".......S.......",
#     "...............",
#     ".......^.......",
#     "...............",
#     "......^.^......",
#     "...............",
#     ".....^.^.^.....",
#     "...............",
#     "....^.^...^....",
#     "...............",
#     "...^.^...^.^...",
#     "...............",
#     "..^...^.....^..",
#     "...............",
#     ".^.^.^.^.^...^.",
#     "...............",
# ]

diagram: list[str] = []
with open("input1.txt") as f:
    for line in f.readlines():
        diagram.append(line.strip())

rows = len(diagram)
cols = len(diagram[0])

beams: set[Point] = set()
splitters: set[Point] = set()
visited: set[Point] = set()

for y in range(rows):
    for x in range(cols):
        if diagram[y][x] == "S":
            beams.add(Point(y, x))
        elif diagram[y][x] == "^":
            splitters.add(Point(y, x))

while beams:
    beam = beams.pop()
    while beam not in splitters and beam.y < rows:
        visited.add(beam)
        beam = Point(beam.y + 1, beam.x)
    if beam in splitters:
        beams.add(Point(beam.y, beam.x - 1))
        beams.add(Point(beam.y, beam.x + 1))

count = 0
for splitter in splitters:
    if Point(splitter.y - 1, splitter.x) in visited:
        count += 1
print(count)
