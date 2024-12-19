def is_possible(towels: list[str], design: str, pos: int = 0) -> bool:
    if pos == len(design):
        return True

    for towel in towels:
        if design.startswith(towel, pos):
            if is_possible(towels, design, pos + len(towel)):
                return True
    return False


with open('input1.txt') as file:
    data = list(map(lambda x: x.replace('\n', ''), file.readlines()))

towels = data[0].split(', ')
designs = [d for d in data[2:]]

possible_designs = 0
for design in designs:
    if is_possible(towels, design):
        possible_designs += 1

print(possible_designs)
