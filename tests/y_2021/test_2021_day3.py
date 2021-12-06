from unittest.mock import mock_open, patch

from y_2021.common import load_input
from y_2021.day3 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test_complete():
    day._input_data = load_input(__name__.replace("test_2021_day", ""), 1)
    print(day._input_data)
    day._preprocess_input()
    assert day._calculate_1() == 198
    assert day._calculate_2() == 230
