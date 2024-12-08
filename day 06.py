# day 06
# it does take a couple mins to finish part 2
from math import floor

data = [[i for i in line.strip()] for line in open("day 06 data.txt").readlines()]

# defines the direction she can move in
# +1 index = 90* right
# start index = facing up
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
direction_index = 2

# find initial position of guard
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "^":
            STARTING_POSITION = [i, j]


# part 1
lab_layout = [[digit for digit in line] for line in data]
lab_layout[STARTING_POSITION[0]][STARTING_POSITION[1]] = "X"
position = [STARTING_POSITION[0], STARTING_POSITION[1]]

while 0 <= position[0] + directions[direction_index][0] < len(
    lab_layout
) and 0 <= position[1] + directions[direction_index][1] < len(lab_layout[0]):
    position[0] = position[0] + directions[direction_index][0]
    position[1] = position[1] + directions[direction_index][1]
    if lab_layout[position[0]][position[1]] == "#":
        position[0] = position[0] - directions[direction_index][0]
        position[1] = position[1] - directions[direction_index][1]
        direction_index = (direction_index + 1) % 4
    else:
        lab_layout[position[0]][position[1]] = "X"

output = "".join(["".join([i for i in line]) for line in lab_layout])
total = output.count("X")
print(total)
# print(data)


# part 2
def check_for_loop(STARTING_POSITION, lab_layout):
    position = [
        STARTING_POSITION[0],
        STARTING_POSITION[1],
    ]  # forces pass by value cause python is dumb
    turn_on_plus = 0
    direction_index = 2
    while 0 <= position[0] + directions[direction_index][0] < len(
        lab_layout
    ) and 0 <= position[1] + directions[direction_index][1] < len(lab_layout[0]):
        position[0] = position[0] + directions[direction_index][0]
        position[1] = position[1] + directions[direction_index][1]
        if lab_layout[position[0]][position[1]] == "#":
            position[0] = position[0] - directions[direction_index][0]
            position[1] = position[1] - directions[direction_index][1]
            direction_index = (direction_index + 1) % 4
            if lab_layout[position[0]][position[1]] == "+":
                turn_on_plus += 1
            else:
                lab_layout[position[0]][position[1]] = "+"
        else:
            if direction_index % 2:  # horizonbtal
                if lab_layout[position[0]][position[1]] == ".":
                    lab_layout[position[0]][position[1]] = "-"
                elif lab_layout[position[0]][position[1]] == "|":
                    lab_layout[position[0]][position[1]] = "+"
            else:  # vertical
                if lab_layout[position[0]][position[1]] == ".":
                    lab_layout[position[0]][position[1]] = "|"
                elif lab_layout[position[0]][position[1]] == "-":
                    lab_layout[position[0]][position[1]] = "+"
        if turn_on_plus > 10:
            return True
    return False


to_check = len(data) * len(data[0])
checked = 0
percent_checked = -1
total = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        checked += 1
        lab_layout = [
            [digit for digit in line] for line in data
        ]  # forces pass by value cause python is dumb
        lab_layout[STARTING_POSITION[0]][STARTING_POSITION[1]] = "."
        if STARTING_POSITION != [i, j] and data[i][j] != "#":
            lab_layout[i][j] = "#"
            # print(lab_layout, STARTING_POSITION)
            total += int(check_for_loop(STARTING_POSITION, lab_layout))
        if floor(checked / to_check * 100) > percent_checked:
            percent_checked = floor(checked / to_check * 100)
print(total)
