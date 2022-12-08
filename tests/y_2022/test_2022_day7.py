from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2022.common import load_input
from y_2022.day7 import Day

with patch("builtins.open", mock_open(read_data="$ ls")):
    day = Day()


def test__preprocess_input():
    day._input_data = [["$ cd /", "$ cd a"]]
    day._preprocess_input()
    assert list(day._Day__folders.keys()) == ["/", "/#a"]


def test_complete():
    day._input_data = load_input(7, 1)
    day._preprocess_input()
    assert day._calculate_1() == 95437
    assert day._calculate_2() == 24933642
