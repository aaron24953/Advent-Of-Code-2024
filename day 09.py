# day 09

data = [int(i) for i in open("day 09 data.txt").readline().strip()]

disk = []
file = True
id = 0
for digit in data:
    if file:
        for i in range(digit):
            disk.append(id)
    else:
        for i in range(digit):
            disk.append(-1)
    id += int(file)
    file = not file


# part 1
# part_disk = [i for i in disk]
# while part_disk.count(-1) > 0:
#     value = part_disk.pop()
#     if value != -1:
#         part_disk[part_disk.index(-1)] = value

# checksum = 0
# for i in range(len(part_disk)):
#     checksum += i * part_disk[i]

# print(checksum)

# part 2

i = len(disk) - 1
while i > 0:
    if disk[i] == -1:
        i -= 1
    else:
        id = disk[i]
        j = 1
        while disk[i - j] == id and i - j > 0:
            j += 1

        gap = 0
        for k in range(i):
            if disk[k] == -1:
                gap += 1
            else:
                gap = 0
            if gap == j:
                for l in range(gap):
                    disk[i - l] = -1
                    disk[k - l] = id
                break
        i -= j


checksum = 0
for i in range(len(disk)):
    if disk[i] > 0:
        checksum += i * disk[i]

print(checksum)
