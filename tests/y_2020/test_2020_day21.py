from unittest.mock import mock_open, patch

from y_2020.day21 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = []
    day._preprocess_input()
    assert day._Day__input == []


def test_calculate_1():
    print()
    day._input_data = []
    day._preprocess_input()
    assert day._calculate_1() == 0


def test_calculate_2():
    print()
    day._input_data = []
    day._preprocess_input()
    assert day._calculate_2() == 0
