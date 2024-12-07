# day 01

data = open("day 01 data.txt").readlines()
data = [line.strip().split("   ") for line in data]
lists = [[], []]
for line in data:
    lists[0].append(int(line[0]))
    lists[1].append(int(line[1]))
lists[0].sort()
lists[1].sort()

# answer for part 1

difference = 0
for i in range(len(lists[0])):
    difference += abs(lists[0][i] - lists[1][i])

print(difference)

# answer for part 2

total = 0
for number in lists[0]:
    total += number * lists[1].count(number)

print(total)
