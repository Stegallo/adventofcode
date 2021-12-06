from unittest.mock import mock_open, patch

from y_2021.common import load_input
from y_2021.day4 import Day

with patch("builtins.open", mock_open(read_data=",")):
    day = Day()


def test_complete():
    day._input_data = load_input(__name__.replace("test_2021_day", ""), 1)
    day._preprocess_input()
    assert day._calculate_1() == 4512
    assert day._calculate_2() == 1924
