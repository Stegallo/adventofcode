def decode_seat(x):
    t = 0
    for j, i in enumerate(x[:7]):
        if i == "B":
            t += 2 ** (6 - j)
    u = 0
    for j, i in enumerate(x[7:]):
        if i == "R":
            u += 2 ** (2 - j)
    return t * 8 + u


def calculate_1(x):
    t = 0
    for i in x:
        c = decode_seat(i)
        if c > t:
            t = c
    return t


def calculate_2(x):
    seats = sorted([decode_seat(i) for i in x])
    for i, j in enumerate((seats)):
        if i == 0:
            continue
        if not (seats[i] == seats[i - 1] + 1):
            return j - 1
    return 0
