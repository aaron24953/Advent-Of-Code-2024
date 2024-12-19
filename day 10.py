# day 10

data = [
    [int(digit) for digit in line.strip()]
    for line in open("day 10 data.txt").readlines()
]


# both parts lmao
otherTotal = 0
total = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 0:
            layer = [(i, j)]
            height = 0
            while height < 9 and layer:
                nextLayer = []
                for potential in layer:
                    if data[potential[0]][potential[1]] == height:
                        nextLayer.append(
                            (
                                max(0, min(len(data) - 1, potential[0] + 1)),
                                max(0, min(len(data[0]) - 1, potential[1])),
                            )
                        )
                        nextLayer.append(
                            (
                                max(0, min(len(data) - 1, potential[0])),
                                max(0, min(len(data[0]) - 1, potential[1] + 1)),
                            )
                        )
                        nextLayer.append(
                            (
                                max(0, min(len(data) - 1, potential[0] - 1)),
                                max(0, min(len(data[0]) - 1, potential[1])),
                            )
                        )
                        nextLayer.append(
                            (
                                max(0, min(len(data) - 1, potential[0])),
                                max(0, min(len(data[0]) - 1, potential[1] - 1)),
                            )
                        )

                layer = [i for i in nextLayer]
                height += 1

            peaks = []
            for potential in layer:
                if data[potential[0]][potential[1]] == 9:
                    peaks.append(potential)

            otherTotal += len(peaks)
            peaks = set(map(tuple, peaks))
            total += len(peaks)

print(total, otherTotal)
