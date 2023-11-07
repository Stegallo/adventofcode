from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2015.day6 import Day

with patch("builtins.open", mock_open(read_data="command 0,0 through 999,999")):
    day = Day()


def test_calculate_1():
    day._input_data = [["turn on 0,0 through 9,0", "turn off 8,0 through 9,0"]]
    day._preprocess_input()
    assert day._calculate_1() == 8

    day._input_data = [["turn off 0,0 through 9,0"]]
    day._preprocess_input()
    assert day._calculate_1() == 0

    day._input_data = [["toggle 0,0 through 9,0"]]
    day._preprocess_input()
    assert day._calculate_1() == 10


def test_calculate_2():
    day._input_data = [["turn on 0,0 through 0,0"]]
    day._preprocess_input()
    assert day._calculate_2() == 1

    day._input_data = [["turn off 0,0 through 0,0"]]
    day._preprocess_input()
    assert day._calculate_2() == 0

    day._input_data = [["toggle 0,0 through 0,0"]]
    day._preprocess_input()
    assert day._calculate_2() == 2
