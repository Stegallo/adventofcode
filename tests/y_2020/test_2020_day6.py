from unittest.mock import mock_open, patch

from y_2020.day6 import Day

with patch("builtins.open", mock_open(read_data=":")):
    day = Day()


def test_calculate_1():
    day._input_data = day._preprocess_input(
        [
            "abc",
            "",
            "a",
            "b",
            "c",
            "",
            "ab",
            "ac",
            "",
            "a",
            "a",
            "a",
            "a",
            "",
            "b",
        ]
    )
    assert day._calculate_1() == 11


def test_calculate_2():
    day._input_data = day._preprocess_input(
        [
            "abc",
            "",
            "a",
            "b",
            "c",
            "",
            "ab",
            "ac",
            "",
            "a",
            "a",
            "a",
            "a",
            "",
            "b",
        ]
    )
    assert day._calculate_2() == 6
