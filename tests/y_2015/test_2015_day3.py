from y_2015.day3 import calculate_1, calculate_2


def test_calculate_1():
    assert calculate_1(">") == 2
    assert calculate_1("^>v<") == 4
    assert calculate_1("^v^v^v^v^v") == 2


def test_calculate_2():
    assert calculate_2("^v") == 3
    assert calculate_2("^>v<") == 3
    assert calculate_2("^v^v^v^v^v") == 11
