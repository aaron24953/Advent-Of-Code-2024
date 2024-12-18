# day 08
data = [[i for i in line.strip()] for line in open("day 08 data.txt").readlines()]


# part 1
antinodes = [["" for i in line] for line in data]
for i in range(len(data)):
    for j in range(len(data[i])):
        antenna = data[i][j]
        if antenna != ".":
            for k in range(len(data)):
                for l in range(len(data[i])):
                    if data[k][l] == antenna and not (i == k and j == l):
                        if 0 <= i + i - k < len(data) and 0 <= j + j - l < len(data[i]):
                            antinodes[i + i - k][j + j - l] = "#"
                        if 0 <= k + k - i < len(data) and 0 <= l + l - j < len(data[i]):
                            antinodes[k + k - i][l + l - j] = "#"

compressedAntinodes = "\n".join([".".join(line) for line in antinodes])
print(compressedAntinodes.count("#"))


# part 2
antinodes = [["" for i in line] for line in data]
for i in range(len(data)):
    for j in range(len(data[i])):
        antenna = data[i][j]
        if antenna != ".":
            for k in range(len(data)):
                for l in range(len(data[i])):
                    if data[k][l] == antenna and not (i == k and j == l):
                        antinodes[i][j] = "#"
                        antinodes[k][l] = "#"
                        m = 1
                        while 0 <= i + m * (i - k) < len(data) and 0 <= j + m * (
                            j - l
                        ) < len(data[i]):
                            antinodes[i + m * (i - k)][j + m * (j - l)] = "#"
                            m += 1
                        m = 1
                        while 0 <= k + m * (k - i) < len(data) and 0 <= l + m * (
                            l - j
                        ) < len(data[i]):
                            antinodes[k + m * (k - i)][l + m * (l - j)] = "#"
                            m += 1

compressedAntinodes = "\n".join([".".join(line) for line in antinodes])
print(compressedAntinodes.count("#"))
