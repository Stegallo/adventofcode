def decode_seat(x):
    row = sum(2 ** (6 - c) for c, value in enumerate(x[:7]) if value == "B")
    column = sum(2 ** (2 - c) for c, value in enumerate(x[7:]) if value == "R")
    return row * 8 + column


def calculate_1(x):
    return max([decode_seat(i) for i in x])


def calculate_2(x):
    seats = sorted([decode_seat(i) for i in x])
    for c, value in enumerate((seats)):
        if seats[c] != seats[c + 1] - 1:
            return value + 1
    return 0
