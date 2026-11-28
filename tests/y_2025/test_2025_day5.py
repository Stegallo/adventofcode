# Example + expected answers from the 2025 day 5 puzzle.
from unittest.mock import mock_open, patch

from y_2025.day5 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""3-5
10-14
16-20
12-18

1
5
8
11
17
32""",
    ),
):
    day = Day()


def test__preprocess_input():
    day._preprocess_input()
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 3


def test_calculate_2():
    r = day._calculate_2()
    assert r == 14
