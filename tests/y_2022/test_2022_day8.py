from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2022.common import load_input
from y_2022.day8 import Day

with patch("builtins.open", mock_open(read_data="01\n23")):
    day = Day()


def test__preprocess_input():
    day._input_data = [["01", "23"]]
    day._preprocess_input()
    assert day._Day__grid == {(0, 0): "0", (0, 1): "1", (1, 0): "2", (1, 1): "3"}


def test_complete():
    day._input_data = load_input(8, 1)
    day._preprocess_input()
    assert day._calculate_1() == 21
    assert day._calculate_2() == 8
