from y_2020.day1 import Day
from unittest.mock import patch, mock_open

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test_calculate_1():
    day._input_data = [1721, 979, 366, 299, 675, 1456]
    assert day._calculate_1() == 514579
    day._input_data = []
    assert day._calculate_1() == 0


def test_calculate_2():
    day._input_data = [1721, 979, 366, 299, 675, 1456]
    assert day._calculate_2() == 241861950
    day._input_data = []
    assert day._calculate_2() == 0
