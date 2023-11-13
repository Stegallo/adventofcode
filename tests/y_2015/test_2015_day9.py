from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2015.day9 import Day

with patch("builtins.open", mock_open(read_data="London to Dublin = 464")):
    day = Day()


def test_calculate_1():
    day._input_data = [
        [
            "London to Dublin = 464",
            "London to Belfast = 518",
            "Dublin to Belfast = 141",
        ],
    ]
    day._preprocess_input()
    assert day._calculate_1() == 605


def test_calculate_2():
    day._input_data = [
        [
            "London to Dublin = 464",
            "London to Belfast = 518",
            "Dublin to Belfast = 141",
        ],
    ]
    day._preprocess_input()
    assert day._calculate_2() == 982
