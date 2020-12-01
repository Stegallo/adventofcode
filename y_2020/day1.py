def calculate_1(x):
    y = [int(i) for i in x]

    for i in y:
        for j in y:
            if (i + j) == 2020:
                return i * j

    return 0


def calculate_2(x):
    y = [int(i) for i in x]

    for i in y:
        for j in y:
            for k in y:
                if (i + j + k) == 2020:
                    return i * j * k

    return 0
