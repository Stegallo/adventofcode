from unittest.mock import mock_open, patch

from y_2022.common import load_input
from y_2022.day1 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    day._input_data = []
    day._preprocess_input()
    assert day._Day__input_data == []

    day._input_data = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]
    day._preprocess_input()
    assert day._Day__input_data == [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]
