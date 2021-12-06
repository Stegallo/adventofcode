from unittest.mock import mock_open, patch

from y_2021.common import load_input
from y_2021.day1 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    day._input_data = [
        "199",
        "200",
        "208",
        "210",
        "200",
        "207",
        "240",
        "269",
        "260",
        "263",
    ]
    day._preprocess_input()
    assert day._Day__input_data == [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    day._input_data = []
    day._preprocess_input()
    assert day._Day__input_data == []


def test_calculate_1():
    day._Day__input_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert day._calculate_1() == 7
    day._Day__input_data = []
    assert day._calculate_1() == 0


def test_calculate_2():
    day._Day__input_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert day._calculate_2() == 5
    day._Day__input_data = []
    assert day._calculate_2() == 0


def test_complete():
    day._input_data = load_input(1, 1)
    day._preprocess_input()
    assert day._calculate_1() == 7
    assert day._calculate_2() == 5
