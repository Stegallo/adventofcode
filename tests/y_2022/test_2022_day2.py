from unittest.mock import mock_open, patch

from y_2022.common import load_input
from y_2022.day2 import Day

with patch("builtins.open", mock_open(read_data="0")):
    day = Day()


def test__preprocess_input():
    day._input_data = [[]]
    day._preprocess_input()
    assert day._Day__input_data == []

    day._input_data = [
        ["A Y", "B X", "C Z"],
    ]
    day._preprocess_input()
    assert day._Day__input_data == ["A Y", "B X", "C Z"]


def test_complete():
    day._input_data = load_input(2, 1)
    day._preprocess_input()
    assert day._calculate_1() == 15
    assert day._calculate_2() == 12
