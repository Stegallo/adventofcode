from unittest.mock import mock_open, patch

from y_2020.day2 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    day._input_data = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]
    day._preprocess_input()
    assert day._Day__password_list == [
        (1, 3, "a", "abcde"),
        (1, 3, "b", "cdefg"),
        (2, 9, "c", "ccccccccc"),
    ]


def test_calculate_1():
    day._Day__password_list = [
        (1, 3, "a", "abcde"),
        (1, 3, "b", "cdefg"),
        (2, 9, "c", "ccccccccc"),
    ]
    assert day._calculate_1() == 2


def test_calculate_2():
    day._Day__password_list = [
        (1, 3, "a", "abcde"),
        (1, 3, "b", "cdefg"),
        (2, 9, "c", "ccccccccc"),
    ]
    assert day._calculate_2() == 1
