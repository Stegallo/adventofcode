from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2022.common import load_input
from y_2022.day3 import Day

with patch("builtins.open", mock_open(read_data="0")):
    day = Day()


def test_get_priority():
    assert day._Day__get_priority("p") == 16
    assert day._Day__get_priority("L") == 38
    assert day._Day__get_priority("P") == 42
    assert day._Day__get_priority("v") == 22
    assert day._Day__get_priority("t") == 20
    assert day._Day__get_priority("s") == 19
    assert day._Day__get_priority("r") == 18
    assert day._Day__get_priority("Z") == 52


def test__preprocess_input():
    day._input_data = [[]]
    day._preprocess_input()
    assert day._Day__input_data == []


def test_complete():
    day._input_data = load_input(3, 1)
    day._preprocess_input()
    assert day._calculate_1() == 157
    assert day._calculate_2() == 70
