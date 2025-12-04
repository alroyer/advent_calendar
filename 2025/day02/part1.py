# ranges = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

with open("input1.txt") as file:
    ranges = file.readline()

sum = 0
for r in ranges.split(","):
    begin, end = r.split("-")
    for n in range(int(begin), int(end) + 1):
        n_str = str(n)
        count = len(n_str)
        if count % 2 == 0:
            count //= 2
            if n_str[:count] == n_str[count:]:
                print(n_str)
                sum += n
print(sum)
