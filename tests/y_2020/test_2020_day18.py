from unittest.mock import mock_open, patch

from y_2020.day18 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = []
    day._preprocess_input()
    assert day._Day__input == []


def test_calculate_1():
    print()
    day._Day__input = ["1 + 2 * 3 + 4 * 5 + 6"]
    assert day._calculate_1() == 71
    day._Day__input = ["1 + (2 * 3) + (4 * (5 + 6))"]
    assert day._calculate_1() == 51
    day._Day__input = ["2 * 3 + (4 * 5)"]
    assert day._calculate_1() == 26
    day._Day__input = ["5 + (8 * 3 + 9 + 3 * 4 * 3)"]
    assert day._calculate_1() == 437
    day._Day__input = ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"]
    assert day._calculate_1() == 12240
    # day._Day__input = ["((2 + 3 * 4) * (5 + 6 * 7 + 8) + 9) + 10 + 11 * 12"]
    # assert day._calculate_1() == 0
    day._Day__input = ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]
    assert day._calculate_1() == 13632


# ((5*4)*(11*15)+9)+10+11*12
# (20*165+9)+10+11*12
# (20*174)+10+11*12
# 3480+10+11*12
# 3501*12
# 42012
def test_calculate_2():
    print()
    # day._Day__input = ["1 + 2 * 3 + 4 * 5 + 6"]
    # assert day._calculate_2() == 231
    # day._Day__input = ["1 + (2 * 3) + (4 * (5 + 6))"]
    # assert day._calculate_1() == 51
    # day._Day__input = ["2 * 3 + (4 * 5)"]
    # assert day._calculate_1() == 46
    # day._Day__input = ["5 + (8 * 3 + 9 + 3 * 4 * 3)"]
    # assert day._calculate_1() == 1445
    # day._Day__input = ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"]
    # assert day._calculate_1() == 669060
    day._Day__input = ["((2 + 3 * 4) * (5 + 6 * 7 + 8) + 9) + 10 + 11 * 12"]
    assert day._calculate_1() == 0
    # day._Day__input = ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]
    # assert day._calculate_1() == 23340
