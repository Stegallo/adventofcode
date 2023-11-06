from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2015.day6 import Day

with patch("builtins.open", mock_open(read_data="1x1x1")):
    day = Day()


def test_calculate_1():
    assert False
    # day._input_data = [["2x3x4"]]
    # day._preprocess_input()
    # assert day._calculate_1() == 58
    #
    # day._input_data = [["1x1x10"]]
    # day._preprocess_input()
    # assert day._calculate_1() == 43


def test_calculate_2():
    assert False
    # day._input_data = [["2x3x4"]]
    # day._preprocess_input()
    # assert day._calculate_2() == 34
    #
    # day._input_data = [["1x1x10"]]
    # day._preprocess_input()
    # assert day._calculate_2() == 14
