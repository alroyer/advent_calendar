from dataclasses import dataclass


@dataclass
class Range:
    destination_range: tuple[int, int]
    source_range: tuple[int, int]


def read_data(path: str) -> list[str]:
    with open(path, 'r') as f:
        data = f.readlines()
        return [d.strip() for d in data]


def parse_data(data: list[str]) -> tuple[list[tuple[int, int]], list[tuple[str, list[Range]]]]:
    seeds = []
    maps = []
    current_map = []
    category = None
    for d in data:
        if d.startswith('seeds'):
            seed_ranges = [int(x) for x in d[7:].split(' ')]
            for n in range(0, len(seed_ranges), 2):
                seeds.append((seed_ranges[n], seed_ranges[n] + seed_ranges[n + 1]))
        elif ':' in d:
            if category:
                maps.append((category, current_map))
            current_map = []
            category = d
        elif d:
            destination, source, length = [int(x) for x in d.split(' ')]
            current_map.append(Range((destination, destination + length), (source, source + length)))
    if category:
        maps.append((category, current_map))
    return seeds, maps


def find_min_location(seeds: list[tuple[int, int]], maps: list[tuple[str, list[Range]]]) -> int:
    locations = []
    for seed in seeds:
        location = seed
        for _, ranges in maps:
            for range_ in ranges:
                # TODO
                start = max(range_.source_range[0], location[0])
                end = min(range_.source_range[1], location[1])
                if start < range_.source_range[1] and end >= range_.source_range[0]:
                    location = (
                        range_.destination_range[0] + (start - range_.source_range[0]),
                        range_.destination_range[0] + (end - range_.source_range[0]),
                    )

                    if location[0] < range_.source_range[0]:
                        seeds.append((location[0], range_.source_range[0]))
                    if location[1] >= range_.source_range[1]:
                        seeds.append((range_.source_range[1], location[1]))
                    break
        locations.append(location)
    return min([l[0] for l in locations])


def main() -> None:
    data = read_data('input0.txt')
    seeds, maps = parse_data(data)
    location = find_min_location(seeds, maps)
    print(f'{location=}')


if __name__ == '__main__':
    main()
