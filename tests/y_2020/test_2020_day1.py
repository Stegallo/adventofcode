from y_2020.day1 import calculate_1, calculate_2


def test_calculate_1():
    assert calculate_1([1721, 979, 366, 299, 675, 1456]) == 514579
    assert calculate_1([]) == 0


def test_calculate_2():
    assert calculate_2([1721, 979, 366, 299, 675, 1456]) == 241861950
    assert calculate_2([]) == 0
