ranges: list[tuple[int, int]] = []
ingredients: list[int] = []

with open("input1.txt") as f:
    range_input = True
    for line in f:
        if line.strip() == "":
            range_input = False
            continue
        if range_input:
            range_input = line.strip()
            begin, end = range_input.split("-")
            ranges.append((int(begin), int(end)))
        else:
            ingredients.append(int(line.strip()))

fresh_ingredients = set()
for begin, end in ranges:
    for ingredient in ingredients:
        if begin <= ingredient <= end:
            fresh_ingredients.add(ingredient)

print(len(fresh_ingredients))
