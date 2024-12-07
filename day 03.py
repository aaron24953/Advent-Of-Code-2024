# day 03
def do_multiplication(multiplication):

    invalid = False

    multiplication = multiplication.split(",")
    if len(multiplication) >= 2:
        multiplication[1] = multiplication[1] + "    "
        try:
            int(multiplication[0])
        except:
            invalid = True
        if multiplication[1][0] in digits and multiplication[1][1] == ")":
            num_digits = 1
        elif (
            multiplication[1][0] in digits
            and multiplication[1][1] in digits
            and multiplication[1][2] == ")"
        ):
            num_digits = 2
        elif (
            multiplication[1][0] in digits
            and multiplication[1][1] in digits
            and multiplication[1][2] in digits
            and multiplication[1][3] == ")"
        ):
            num_digits = 3
        else:
            invalid = True
    else:
        invalid = True
    if not invalid:
        return int(multiplication[0]) * int(multiplication[1][:num_digits])
    else:
        return -1


data = "".join([line.strip() for line in open("day 03 data.txt").readlines()])
digits = [str(i) for i in range(10)]

# part 1
multiplications = data.split("mul(")
total = 0
for multiplication in multiplications:

    value = do_multiplication(multiplication)
    if value > 0:
        total += value

print(total)

# part 2
split_do = data.split("do")
do = True
multiplications = ""
for part in split_do:
    part = part + "          "
    if part[:2] == "()":
        do = True
    elif part[:5] == "n't()":
        do = False
    if do:
        multiplications = multiplications + "do" + part


multiplications = multiplications.split("mul(")
total = 0
for multiplication in multiplications:

    value = do_multiplication(multiplication)
    if value > 0:
        total += value

print(total)
