def extract(i):
    return int(i[0].split("-")[0]), int(i[0].split("-")[1]), i[1].split(":")[0], i[2]


def valid1(i):
    min, max, char, pwd = extract(i)

    c = pwd.count(char)
    return c >= min and c <= max


def valid2(i):
    min, max, char, pwd = extract(i)

    one = 0
    two = 0
    if pwd[min - 1] == char:
        one = 1
    if pwd[max - 1] == char:
        two = 1
    return one + two == 1


def calculate_1(x):
    y = [i.split(" ") for i in x]
    return sum(1 for i in y if valid1(i))


def calculate_2(x):
    y = [i.split(" ") for i in x]
    return sum(1 for i in y if valid2(i))
