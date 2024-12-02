from numpy import diff as npdiff

safe_count = 0

with open('input1.txt') as f:
    data = f.readline()
    while data:
        report = [int(x) for x in data.split()]
        diffs = npdiff(report)

        max_diff = max(abs(min(diffs)), abs(max(diffs)))

        all_positif = all([n > 0 for n in diffs])
        all_negatif = all([n < 0 for n in diffs])

        if max_diff <= 3 and (all_positif or all_negatif):
            safe_count += 1

        data = f.readline()

print(safe_count)
