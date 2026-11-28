# Example + expected answers from the 2025 day 9 puzzle.
from unittest.mock import mock_open, patch

from y_2025.day9 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""",
    ),
):
    day = Day()


def test__preprocess_input():
    day._preprocess_input()
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 50


def test_calculate_2():
    r = day._calculate_2()
    assert r == 24
