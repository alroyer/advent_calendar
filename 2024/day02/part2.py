from numpy import diff as npdiff


def is_safe(report):
    diffs = npdiff(report)

    max_diff = max(abs(min(diffs)), abs(max(diffs)))

    all_positif = all([n > 0 for n in diffs])
    all_negatif = all([n < 0 for n in diffs])

    return max_diff <= 3 and (all_positif or all_negatif)


safe_count = 0

with open('input1.txt') as f:
    data = f.readline()
    while data:
        report = [int(x) for x in data.split()]

        if is_safe(report):
            safe_count += 1
        else:
            for index in range(len(report)):
                new_report = report.copy()
                del new_report[index]
                if is_safe(new_report):
                    safe_count += 1
                    break

        data = f.readline()

print(safe_count)
