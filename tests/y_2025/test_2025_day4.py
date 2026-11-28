# Example + expected answers from the 2025 day 4 puzzle.
from unittest.mock import mock_open, patch

from y_2025.day4 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""",
    ),
):
    day = Day()


def test__preprocess_input():
    day._preprocess_input()
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 13


def test_calculate_2():
    r = day._calculate_2()
    assert r == 43
