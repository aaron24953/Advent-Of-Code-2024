# day 05

data = [line.strip() for line in open("day 05 data.txt").readlines()]

rules = [[] for i in range(100)]
for line in data:
    line = line.split("|")
    if len(line) == 2:
        rules[int(line[0])].append(int(line[1]))

manuals = []
for line in data:
    line = line.split(",")
    if len(line) > 2:
        manuals.append([int(i) for i in line])


def check_manual(manual):
    valid = True
    for i in range(1, len(manual)):
        if rules[manual[i]]:
            for j in range(i):
                if manual[j] in rules[manual[i]]:
                    valid = False
    return valid


# part 1
total = 0
for manual in manuals:
    if check_manual(manual):
        total += manual[(len(manual) - 1) // 2]
print(total)

# part 2
total = 0
for manual in manuals:
    if not check_manual(manual):
        while True:
            for i in range(1, len(manual)):
                if rules[manual[i]]:
                    for j in range(i):
                        if manual[j] in rules[manual[i]]:
                            temp = manual[j]
                            manual[j] = manual[i]
                            manual[i] = temp
                            break
            if check_manual(manual):
                break
        total += manual[(len(manual) - 1) // 2]
print(total)
