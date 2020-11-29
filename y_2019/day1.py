def inner_1(i):
    return i // 3 - 2


def calculate_1(x):
    return sum(inner_1(int(i)) for i in x)


def inner_2(i):
    if (w := inner_1(i)) < 0:
        return 0
    return w + inner_2(w)


def calculate_2(x):
    return sum(inner_2(int(i)) for i in x)
