from y_2015.day1 import calculate_1, calculate_2


def test_calculate_1():
    assert calculate_1("(())") == 0
    assert calculate_1("()()") == 0
    assert calculate_1("(((") == 3
    assert calculate_1("(()(()(") == 3
    assert calculate_1("))(((((") == 3
    assert calculate_1("())") == -1
    assert calculate_1("))(") == -1
    assert calculate_1(")))") == -3
    assert calculate_1(")())())") == -3


def test_calculate_2():
    assert calculate_2(")") == 1
    assert calculate_2("()())") == 5
