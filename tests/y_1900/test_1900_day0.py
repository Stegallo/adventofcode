from __future__ import annotations

from unittest.mock import mock_open, patch

from y_1900.day0 import Day

with patch("builtins.open", mock_open(read_data="0")):
    day = Day()


def test__preprocess_input():
    day._input_data = [[]]
    day._preprocess_input()
    assert day._Day__input_data == []


def test_complete():
    day._input_data = day._load_input()
    day._preprocess_input()
    assert day._calculate_1() == 0
    assert day._calculate_2() == 0
