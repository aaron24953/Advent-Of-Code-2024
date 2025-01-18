# day 11

from math import log10, floor
from functools import cache

data = open("day 11 data.txt").readline().strip().split(" ")

# part 1
BLINKS = 25
total = 0
for item in data:
    nextLayer = [int(item)]
    for i in range(BLINKS):
        layer = [item for item in nextLayer]
        nextLayer = []
        for stone in layer:
            if stone == 0:
                nextLayer.append(1)
            elif floor(log10(stone)) % 2:
                length = floor(log10(stone)) + 1
                halfLength = length // 2
                powered10 = 10**halfLength
                nextLayer.append(stone // powered10)
                nextLayer.append(stone % powered10)
            else:
                nextLayer.append(stone * 2024)
    if i < 25:
        total += len(nextLayer)

print(total)


# part 2
@cache
def count(stone, steps):
    if steps == 0:
        return 1
    else:
        steps -= 1
    if stone == 0:
        return count(1, steps)
    elif floor(log10(stone)) % 2:
        length = floor(log10(stone)) + 1
        halfLength = length // 2
        powered10 = 10**halfLength
        return count(stone // powered10, steps) + count(stone % powered10, steps)
    else:
        return count(stone * 2024, steps)


length = sum([count(int(stone), 75) for stone in data])
print(length)
