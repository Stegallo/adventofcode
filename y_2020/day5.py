def decode_seat(x):
    return int("".join(["1" if i in ["B", "R"] else "0" for i in x]), 2)


def calculate_1(x):
    return max(decode_seat(i) for i in x)


def calculate_2(x):
    seats = sorted([decode_seat(i) for i in x])
    for c, value in enumerate((seats)):
        if seats[c] != seats[c + 1] - 1:
            return value + 1
    return 0
