from utils import load_multi_input
from common import run_get_code


def draw(mat, i, s, c):
    d = i[0]
    l = int(i[1:])
    if d == "U":
        for k in range(0, l):
            temp = mat.get("x" + str(s[0] + k) + "y" + str(s[1]), (0, 0))
            if temp[1] > 0:
                u = temp[1]
            else:
                u = c + k
            mat["x" + str(s[0] + k) + "y" + str(s[1])] = (temp[0] + 1, u)
        s[0] = s[0] + l
    if d == "D":
        for k in range(0, l):
            temp = mat.get("x" + str(s[0] - k) + "y" + str(s[1]), (0, 0))
            if temp[1] > 0:
                u = temp[1]
            else:
                u = c + k
            mat["x" + str(s[0] - k) + "y" + str(s[1])] = (temp[0] + 1, u)
        s[0] = s[0] - l
    if d == "R":
        for k in range(0, l):
            temp = mat.get("x" + str(s[0]) + "y" + str(s[1] + k), (0, 0))
            if temp[1] > 0:
                u = temp[1]
            else:
                u = c + k
            mat["x" + str(s[0]) + "y" + str(s[1] + k)] = (temp[0] + 1, u)
        s[1] = s[1] + l
    if d == "L":
        for k in range(0, l):
            temp = mat.get("x" + str(s[0]) + "y" + str(s[1] - k), (0, 0))
            if temp[1] > 0:
                u = temp[1]
            else:
                u = c + k
            mat["x" + str(s[0]) + "y" + str(s[1] - k)] = (temp[0] + 1, u)
        s[1] = s[1] - l
    return c + l


def findxs(mat1, mat2):
    result = []
    for i in mat1:
        if i != "x0y0":
            if mat2.get(i):
                result.append(i)
    return result


def findxs2(mat1, mat2):
    result = []
    for i in mat1:
        if i != "x0y0":
            if mat2.get(i):
                result.append(mat1[i][1] + mat2[i][1])
    return result


def manh(xs):
    min = 10000
    for i in xs:
        x = int(i[1 : i.find("y")])
        y = int(i[i.find("y") + 1 :])
        if abs(x) + abs(y) < min:
            min = abs(x) + abs(y)
    return min


def manh2(xs):
    min = 100000
    for i in xs:
        if i < min:
            min = i
    return min


def calculate_1(l, m):
    d1 = {}
    s1 = [0, 0]
    c1 = 0
    for i in l:
        c1 = draw(d1, i, s1, c1)
    d2 = {}
    s2 = [0, 0]
    c2 = 0
    for i in m:
        c2 = draw(d2, i, s2, c2)

    xs = findxs(d1, d2)
    result = manh(xs)
    return result


def calculate_2(l, m):
    d1 = {}
    s1 = [0, 0]
    c1 = 0
    for i in l:
        c1 = draw(d1, i, s1, c1)
    d2 = {}
    s2 = [0, 0]
    c2 = 0
    for i in m:
        c2 = draw(d2, i, s2, c2)

    xs = findxs2(d1, d2)
    result = manh2(xs)
    return result


def main():
    input_data = load_multi_input()
    l, m = input_data
    res_1 = calculate_1(l, m)
    res_2 = calculate_2(l, m)

    print(f"sol 1: {res_1}")
    print(f"sol 1: {res_2}")


if __name__ == "__main__":
    main()


def test_calculate_1():
    print()
    assert calculate_1(["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"])
    assert (
        calculate_1(
            ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
            ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
        )
        == 159
    )
    assert (
        calculate_1(
            [
                "R98",
                "U47",
                "R26",
                "D63",
                "R33",
                "U87",
                "L62",
                "D20",
                "R33",
                "U53",
                "R51",
            ],
            ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
        )
        == 135
    )


def test_calculate_2():
    assert (
        calculate_2(
            ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
            ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
        )
        == 610
    )
    assert (
        calculate_2(
            [
                "R98",
                "U47",
                "R26",
                "D63",
                "R33",
                "U87",
                "L62",
                "D20",
                "R33",
                "U53",
                "R51",
            ],
            ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
        )
        == 410
    )
