# Example + expected answers from the 2025 day 4 puzzle.
from unittest.mock import mock_open, patch

from y_2025.day4 import Day

EXAMPLE = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def _day() -> Day:
    # Fresh instance per test: _calculate_2 mutates the grid, so a shared
    # instance would make these tests order-dependent.
    with patch("builtins.open", mock_open(read_data=EXAMPLE)):
        return Day()


def test__preprocess_input():
    _day()._preprocess_input()
    assert True


def test_calculate_1():
    assert _day()._calculate_1() == 13


def test_calculate_2():
    assert _day()._calculate_2() == 43
