def calculate_2(i):
    s = str(i)
    good_1 = True
    good_2 = False
    good_3 = True
    for k in range(0, 5):
        if k == 0:
            if s[k] == s[k + 1] and s[k + 1] != s[k + 2]:
                good_2 = True
        if k > 0 and k < 4:
            if s[k - 1] != s[k] and s[k] == s[k + 1] and s[k + 1] != s[k + 2]:
                good_2 = True
        if k == 4:
            if s[k - 1] != s[k] and s[k] == s[k + 1]:
                good_2 = True

        if s[k + 1] < s[k]:
            good_1 = False
            return 0
    if good_2:
        return 1
    return 0


def calculate_1(i):
    s = str(i)
    good_1 = True
    good_2 = False
    for k in range(0, 5):
        if s[k] == s[k + 1]:
            good_2 = True
        if s[k + 1] < s[k]:
            good_1 = False
            return 0
    if good_2:
        return 1
    return 0


def main():
    l = 145852
    u = 616942
    c1 = 0
    c2 = 0
    while l < u:
        c1 = c1 + calculate_1(l)
        c2 = c2 + calculate_2(l)
        l = l + 1

    res_1 = c1
    res_2 = c2

    print(f"sol 1: {res_1}")
    print(f"sol 1: {res_2}")


if __name__ == "__main__":
    main()


def test_calculate_1():
    assert calculate_1(111111) == 1
    assert calculate_1(223450) == 0
    assert calculate_1(123789) == 0


def test_calculate_2():
    print()
    assert calculate_2(112233) == 1
    assert calculate_2(123444) == 0
    assert calculate_2(111122) == 1
    assert calculate_2(223450) == 0
    assert calculate_2(222335) == 1
    assert calculate_2(688889) == 0
