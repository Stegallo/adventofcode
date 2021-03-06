from unittest.mock import mock_open, patch

from y_2020.day1 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    day._input_data = ["1721", "979", "366", "299", "675", "1456"]
    day._preprocess_input()
    assert day._Day__input_data == [1721, 979, 366, 299, 675, 1456]

    day._input_data = []
    day._preprocess_input()
    assert day._Day__input_data == []


def test_calculate_1():
    day._Day__input_data = [1721, 979, 366, 299, 675, 1456]
    assert day._calculate_1() == 514579
    day._Day__input_data = []
    assert day._calculate_1() == 0


def test_calculate_2():
    day._Day__input_data = [1721, 979, 366, 299, 675, 1456]
    assert day._calculate_2() == 241861950
    day._Day__input_data = []
    assert day._calculate_2() == 0
