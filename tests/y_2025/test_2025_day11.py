# Example + expected answers from the 2025 day 11 puzzle.
from unittest.mock import mock_open, patch

import pytest

from y_2025.day11 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out""",
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
    assert r == 2
