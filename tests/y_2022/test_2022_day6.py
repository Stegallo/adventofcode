from unittest.mock import mock_open, patch

from y_2022.common import load_input
from y_2022.day6 import Day

with patch("builtins.open", mock_open(read_data=" ")):
    day = Day()


def test__preprocess_input():
    day._input_data = " "
    day._preprocess_input()
    assert day._Day__input_data == " "


def test_complete():
    day._input_data = load_input(6, 1)
    day._preprocess_input()
    assert day._calculate_1() == 7
    assert day._calculate_2() == 19
