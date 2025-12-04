# ranges = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

with open("input1.txt") as file:
    ranges = file.readline()

visited = set()

sum = 0
for r in ranges.split(","):
    begin, end = r.split("-")
    for n in range(int(begin), int(end) + 1):
        n_str = str(n)
        n_str_len = len(n_str)

        for count in range(1, (n_str_len // 2) + 1):
            n_str_set = set([n_str[i : i + count] for i in range(0, n_str_len, count)])
            if len(n_str_set) == 1:
                if n not in visited:
                    visited.add(n)
                    print(n)
                    sum += n
                break

print(f"\n{sum}")
