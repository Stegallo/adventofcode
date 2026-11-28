# Example + expected answers from the 2025 day 3 puzzle.
from unittest.mock import mock_open, patch

from y_2025.day03 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""987654321111111
811111111111119
234234234234278
818181911112111""",
    ),
):
    day = Day()


def test__preprocess_input():
    day._preprocess_input()
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 357


def test_calculate_2():
    r = day._calculate_2()
    assert r == 3121910778619
