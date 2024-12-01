from dataclasses import dataclass


@dataclass
class Range:
    destination_range_start: int
    source_range_start: int
    range_length: int


def read_data(path: str) -> list[str]:
    with open(path, 'r') as f:
        data = f.readlines()
        return [d.strip() for d in data]


def parse_data(data: list[str]) -> tuple[list[int], list[tuple[str, list[Range]]]]:
    seeds = []
    maps = []
    current_map = []
    category = None
    for d in data:
        if d.startswith('seeds'):
            seeds = [int(x) for x in d[7:].split(' ')]
        elif ':' in d:
            if category:
                maps.append((category, current_map))
            current_map = []
            category = d
        elif d:
            destination, source, length = [int(x) for x in d.split(' ')]
            current_map.append(Range(destination, source, length))
    if category:
        maps.append((category, current_map))
    return seeds, maps


def is_in_range(seed: int, range_: Range) -> int | None:
    if seed in range(range_.source_range_start, range_.source_range_start + range_.range_length):
        return range_.destination_range_start + (seed - range_.source_range_start)
    return None


def find_location(source: int, maps: list[tuple[str, list[Range]]]) -> int:
    location = -1
    for _, ranges in maps:
        destination = None
        for range_ in ranges:
            destination = is_in_range(source, range_)
            if destination:
                location = destination
                source = destination
                break
        if not destination:
            location = source
    return location


def find_min_location(seeds: list[int], maps: list[tuple[str, list[Range]]]) -> int:
    locations = []
    for seed in seeds:
        locations.append(find_location(seed, maps))
    return min(locations)


def main() -> None:
    data = read_data('input1.txt')
    seeds, maps = parse_data(data)
    location = find_min_location(seeds, maps)
    print(f'{location=}')


if __name__ == '__main__':
    main()
