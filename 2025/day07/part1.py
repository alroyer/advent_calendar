from dataclasses import dataclass


@dataclass
class Point:
    y: int
    x: int

    def __hash__(self) -> int:
        return hash((self.y, self.x))


diagram = [
    ".......S.......",
    "...............",
    ".......^.......",
    "...............",
    "......^.^......",
    "...............",
    ".....^.^.^.....",
    "...............",
    "....^.^...^....",
    "...............",
    "...^.^...^.^...",
    "...............",
    "..^...^.....^..",
    "...............",
    ".^.^.^.^.^...^.",
    "...............",
]

rows = len(diagram)
cols = len(diagram[0])

beams: set[Point] = set()
splitters: set[Point] = set()

for y in range(rows):
    for x in range(cols):
        if diagram[y][x] == "S":
            beams.add(Point(y, x))
        elif diagram[y][x] == "^":
            splitters.add(Point(y, x))

count = 0
while beams:
    beam = beams.pop()
    while beam not in splitters and beam.y < rows:
        beam = Point(beam.y + 1, beam.x)
    if beam in splitters:
        lpoint = Point(beam.y, beam.x - 1)
        rpoint = Point(beam.y, beam.x + 1)
        beams.add(lpoint)
        beams.add(rpoint)
        count += 1
print(count)
