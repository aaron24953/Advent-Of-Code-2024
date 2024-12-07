# day 04
XMAS = ["X", "M", "A", "S"]
data = [[XMAS.index(i) for i in j.strip()] for j in open("day 04 data.txt").readlines()]


# part 1
directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

total = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 0:
            for direction in directions:
                valid = True
                for k in range(1, 4):
                    if not (
                        data[min(max(i + direction[0] * k, 0), len(data) - 1)][
                            min(max(j + direction[1] * k, 0), len(data[i]) - 1)
                        ]
                        == k
                        and 0 <= i + direction[0] * k < len(data)
                        and 0 <= j + direction[1] * k < len(data[i])
                    ):
                        valid = False
                total += int(valid)

print(total)

# part 2
data = [[-1 if i == 2 else i for i in line] for line in data]
total = 0
for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) - 1):
        if (
            data[i - 1][j - 1] + data[i + 1][j + 1] == 4
            and data[i + 1][j - 1] + data[i - 1][j + 1] == 4
            and data[i][j] == -1
        ):
            total += 1
print(total)
