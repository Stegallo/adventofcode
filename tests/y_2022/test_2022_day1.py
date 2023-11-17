from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2022.day1 import Day

with patch("builtins.open", mock_open(read_data="0")):
    day = Day()


def test__preprocess_input():
    day._input_data = []
    day._preprocess_input()
    assert day._Day__input_data == []

    day._input_data = [
        ["1000", "2000", "3000"],
        ["4000"],
        ["5000", "6000"],
        ["7000", "8000", "9000"],
        ["10000"],
    ]
    day._preprocess_input()
    assert day._Day__input_data == [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]


def test_calculate_1():
    day._Day__input_data = [
        [1000, 2000, 3000],
        [4000],
    ]
    assert day._calculate_1() == 6000


def test_calculate_2():
    day._Day__input_data = [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
    ]
    assert day._calculate_2() == 41000
