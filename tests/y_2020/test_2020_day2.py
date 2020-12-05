from y_2020.day2 import Day
from unittest.mock import patch, mock_open

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test_calculate_1():
    day._input_data = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]
    assert day._calculate_1() == 2


def test_calculate_2():
    day._input_data = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]
    assert day.calculate_2() == 1
