# Example + expected answers from the 2025 day 6 puzzle.
from unittest.mock import mock_open, patch

from y_2025.day6 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="\n".join(
            [
                "123 328  51 64 ",
                " 45 64  387 23 ",
                "  6 98  215 314",
                "*   +   *   +  ",
            ],
        ),
    ),
):
    day = Day()


def test__preprocess_input():
    day._preprocess_input()
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 4277556


def test_calculate_2():
    r = day._calculate_2()
    assert r == 3263827
