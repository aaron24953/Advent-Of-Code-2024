# day 07
from math import ceil, floor, log


data = [
    [[line.strip().split(":")[0]], line.strip().split(":")[1].strip().split(" ")]
    for line in open("day 07 data.txt").readlines()
]
data = [[[int(i) for i in j] for j in k] for k in data]


# part 1
total = 0
for line in data:
    valid = False
    numbers = line[1]
    for i in range(2 ** (len(numbers) - 1)):
        index = 0
        calculation = [j for j in numbers]
        operators = bin(i)[2:]
        operators = "0" * (len(calculation) - 1 - len(operators)) + operators
        while len(calculation) > 1:
            next_number = calculation.pop(1)
            if operators[index] == "0":
                calculation[0] = calculation[0] + next_number
            else:
                calculation[0] = calculation[0] * next_number
            index += 1
        if calculation[0] == line[0][0]:
            valid = True
            break
    if valid:
        total += line[0][0]
print(total)


# part 2
def tri(number):
    if number == 0:
        return "0"
    out = ""
    for i in range(floor(log(number, 3)), -1, -1):
        out = out + str(number // (3**i))
        number -= int(out[-1]) * (3**i)
    return out


total = 0
num_lines = len(data)
num_lines_done = 0
for line in data:
    valid = False
    numbers = line[1]
    for i in range(3 ** (len(numbers) - 1)):
        index = 0
        calculation = [j for j in numbers]
        operators = tri(i)
        operators = "0" * (len(calculation) - 1 - len(operators)) + operators
        while len(calculation) > 1:
            next_number = calculation.pop(1)
            if operators[index] == "0":
                calculation[0] = calculation[0] + next_number
            elif operators[index] == "1":
                calculation[0] = int(f"{calculation[0]}{next_number}")
            else:
                calculation[0] = calculation[0] * next_number
            index += 1
        if calculation[0] == line[0][0]:
            valid = True
            break
    if valid:
        total += line[0][0]
    num_lines_done += 1
    print(f"{num_lines_done}/{num_lines}")
print(total)
