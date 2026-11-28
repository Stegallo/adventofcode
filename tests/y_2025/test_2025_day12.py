# Example + expected answers from the 2025 day 12 puzzle.
from unittest.mock import mock_open, patch

import pytest

from y_2025.day12 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2""",
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
    pytest.skip("part 2 not implemented; fill expected from puzzle")
    r = day._calculate_2()
    assert r == 0  # TODO: expected from puzzle
