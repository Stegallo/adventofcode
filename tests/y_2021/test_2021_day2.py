from unittest.mock import mock_open, patch

from y_2021.common import load_input
from y_2021.day2 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    day._input_data = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]

    day._preprocess_input()
    assert day._Day__input_data == [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]

    day._input_data = []
    day._preprocess_input()
    assert day._Day__input_data == []


def test_calculate_1():
    day._Day__input_data = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
    assert day._calculate_1() == 150
    day._Day__input_data = []
    assert day._calculate_1() == 0


def test_calculate_2():
    day._Day__input_data = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
    assert day._calculate_2() == 900
    day._Day__input_data = []
    assert day._calculate_2() == 0


def test_complete():
    day._input_data = load_input(__name__.replace("test_2021_day", ""), 1)
    day._preprocess_input()
    assert day._calculate_1() == 150
    assert day._calculate_2() == 900
