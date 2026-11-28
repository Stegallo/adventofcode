# Example + expected answers from the 2025 day 10 puzzle.
from unittest.mock import mock_open, patch

import pytest

from y_2025.day10 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""",
    ),
):
    day = Day()


def test__preprocess_input():
    day._preprocess_input()
    assert True


def test_calculate_1():
    pytest.skip("part 1 not implemented; fill expected from puzzle")
    r = day._calculate_1()
    assert r == 0  # TODO: expected from puzzle


def test_calculate_2():
    r = day._calculate_2()
    assert r == 33
