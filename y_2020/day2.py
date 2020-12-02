def extract(x):
    i = x.split(" ")
    return int(i[0].split("-")[0]), int(i[0].split("-")[1]), i[1].split(":")[0], i[2]


def valid1(i):
    min, max, char, pwd = extract(i)

    c = pwd.count(char)
    return c >= min and c <= max


def valid2(i):
    min, max, char, pwd = extract(i)

    return (pwd[min - 1] == char) != (pwd[max - 1] == char)


def calculate_1(x):
    return sum(1 for i in x if valid1(i))


def calculate_2(x):
    return sum(1 for i in x if valid2(i))
