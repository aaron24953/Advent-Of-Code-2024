# day 12

data = [
    [letter for letter in line.strip()] for line in open("day 12 data.txt").readlines()
]

# generates number regions
# part 1
index = 0
sizes = []
perimeters = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if type(data[i][j]) == str:
            size = 0
            perimeter = 0
            letter = data[i][j]
            toCheck = [[i, j]]
            while toCheck:
                nextCheck = toCheck.pop()
                if data[nextCheck[0]][nextCheck[1]] == letter:
                    data[nextCheck[0]][nextCheck[1]] = index
                    size += 1

                    adjacents = [
                        [nextCheck[0] + 1, nextCheck[1]],
                        [nextCheck[0] - 1, nextCheck[1]],
                        [nextCheck[0], nextCheck[1] + 1],
                        [nextCheck[0], nextCheck[1] - 1],
                    ]

                    for adjacent in adjacents:
                        if not (0 <= adjacent[0] < len(data)) or not (
                            0 <= adjacent[1] < len(data[i])
                        ):
                            perimeter += 1
                        elif data[adjacent[0]][adjacent[1]] == letter:
                            toCheck.append([adjacent[0], adjacent[1]])
                        elif data[adjacent[0]][adjacent[1]] != index:
                            perimeter += 1

            sizes.append(size)
            perimeters.append(perimeter)
            index += 1

print(sum([perimeters[i] * sizes[i] for i in range(len(sizes))]))

# part 2

# add ring of -1 for easier edge detection
data.insert(0, [-1 for i in range(len(data[1]))])
data.append([-1 for i in range(len(data[1]))])
for i in range(len(data)):
    data[i].insert(0, -1)
    data[i].append(-1)

sidess = []
index = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == index:
            sides = 0
            toCheck = [[i, j]]
            checked = []
            while toCheck:
                nextCheck = toCheck.pop()
                checked.append(nextCheck)
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for direction in directions:
                    if (
                        data[nextCheck[0] + direction[0]][nextCheck[1] + direction[1]]
                        == index
                        and not [
                            nextCheck[0] + direction[0],
                            nextCheck[1] + direction[1],
                        ]
                        in checked
                        and not [
                            nextCheck[0] + direction[0],
                            nextCheck[1] + direction[1],
                        ]
                        in toCheck
                    ):
                        toCheck.append(
                            [nextCheck[0] + direction[0], nextCheck[1] + direction[1]]
                        )
                for k in range(4):
                    length = -1
                    left = 1
                    right = 1
                    while left or right:
                        if left:
                            if (
                                data[nextCheck[0] + directions[-1][0] * left][
                                    nextCheck[1] + directions[-1][1] * left
                                ]
                                == index
                                and data[
                                    nextCheck[0]
                                    + directions[0][0]
                                    + directions[-1][0] * left
                                ][
                                    nextCheck[1]
                                    + directions[0][1]
                                    + directions[-1][1] * left
                                ]
                                != index
                            ):
                                left += 1
                            else:
                                length += left
                                left = 0
                        if right:
                            if (
                                data[nextCheck[0] + directions[1][0] * right][
                                    nextCheck[1] + directions[1][1] * right
                                ]
                                == index
                                and data[
                                    nextCheck[0]
                                    + directions[0][0]
                                    + directions[1][0] * right
                                ][
                                    nextCheck[1]
                                    + directions[0][1]
                                    + directions[1][1] * right
                                ]
                                != index
                            ):
                                right += 1
                            else:
                                length += right
                                right = 0
                    if (
                        data[nextCheck[0] + directions[0][0]][
                            nextCheck[1] + directions[0][1]
                        ]
                        != index
                    ):
                        sides += 1 / length
                    directions.insert(0, directions.pop())
            sidess.append(round(sides))
            index += 1


print(sum([sidess[i] * sizes[i] for i in range(len(sizes))]))
