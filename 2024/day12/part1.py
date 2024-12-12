from dataclasses import dataclass


def print_map(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            print(map[y][x], end='')
        print()


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True)
class Plot:
    plant: str
    edges: int
    points: list[Point]

    def price(self):
        return self.edges * len(self.points)


with open('input3.txt') as f:
    data = f.read()

map = list(data.split())

print_map(map)

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

height = len(map)
width = len(map[0])

visited = set()
plots = []

for y in range(height):
    for x in range(width):
        p = Point(x, y)
        if p in visited:
            continue

        plant = map[p.y][p.x]

        to_visite = set()
        to_visite.add(p)

        edges = 0
        points = []

        while to_visite:
            p = to_visite.pop()

            visited.add(p)
            points.append(p)

            for d in directions:
                pp = Point(p.x + d[1], p.y + d[0])

                if pp.y < 0 or pp.y >= height or pp.x < 0 or pp.x >= width:
                    edges += 1
                    continue

                pp_plant = map[pp.y][pp.x]
                if plant == pp_plant:
                    if pp in visited:
                        continue
                    to_visite.add(pp)
                else:
                    edges += 1

        plots.append(Plot(plant, edges, points))

total = 0
for plot in plots:
    print(plot, plot.price())
    total += plot.price()
print(total)
