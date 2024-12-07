# day 02

data = open("day 02 data.txt").readlines()
data = [line.strip().split() for line in data]
data = [[int(i) for i in j] for j in data]


def check_safety(report):
    safe = True
    if report[0] > report[1]:  # descending
        previous = -1
        for level in report:
            if previous != -1:
                if not (0 < (previous - level) < 4):
                    safe = False
            previous = level

    elif report[0] < report[1]:  # ascending
        previous = -1
        for level in report:
            if previous != -1:
                if not (0 < (level - previous) < 4):
                    safe = False
            previous = level

    else:
        safe = False
    if safe:
        return True
    else:
        return False


# part 1
safes = 0
for report in data:
    safes += int(check_safety(report))
print(safes)


# part 2
safes = 0
for report in data:
    safe = False
    for i in range(len(report)):
        removed_value = report.pop(i)
        safe = safe or check_safety(report)
        report.insert(i, removed_value)
    safes += int(safe)
print(safes)
