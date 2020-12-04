import re


def extract(x):
    regex = "([\d]+)-([\d]+) ([\D]): ([\D]*)$"
    elements = re.findall(regex, x)[0]
    return int(elements[0]), int(elements[1]), elements[2], elements[3]


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
