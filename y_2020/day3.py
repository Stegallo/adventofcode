def calculate_1(x, a=3, b=1):
    pos = (0, 0)
    c = 0
    while True:
        pos = ((pos[0] + a) % len(x[0]), pos[1] + b)
        if pos[1] >= len(x):
            break
        if x[pos[1]][pos[0]] == "#":
            c += 1
    return c


def calculate_2(x):
    i = 1
    for a in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        i = i * calculate_1(x, *a)
    return i
