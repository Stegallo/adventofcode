from unittest.mock import mock_open, patch

from y_2020.day15 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = ["0,3,6"]
    day._preprocess_input()
    assert day._Day__input == ["0,3,6"]


def test_calculate_1():
    print()
    day._Day__input = ["0,3,6"]
    assert day._calculate_1() == 436


def test_calculate_2():
    print()
    day._Day__input = ["0,3,6"]
    assert day._calculate_2() == 175594
