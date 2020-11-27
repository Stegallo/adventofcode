from y_2019.day1 import calculate_1, calculate_2


def test_calculate_1():
    assert calculate_1(12) == 2
    assert calculate_1(14) == 2
    assert calculate_1(1969) == 654
    assert calculate_1(100756) == 33583


def test_calculate_2():
    assert calculate_2(14) == 2
    assert calculate_2(1969) == 966
    assert calculate_2(100756) == 50346
