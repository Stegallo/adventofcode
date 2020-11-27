from y_2015.day2 import calculate_1, calculate_2


def test_calculate_1():
    assert calculate_1("2x3x4") == 58
    assert calculate_1("1x1x10") == 43


def test_calculate_2():
    assert calculate_2("2x3x4") == 34
    assert calculate_2("1x1x10") == 14
