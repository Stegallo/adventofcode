from unittest.mock import mock_open, patch

from y_2020.day5 import Day

with patch("builtins.open", mock_open(read_data=":")):
    day = Day()


def test_preprocess_input():
    day._input_data = ["FBFBBFFRLR"]
    day._preprocess_input()
    assert day._Day__decoded_seats == [357]

    day._input_data = ["BFFFBBFRRR"]
    day._preprocess_input()
    assert day._Day__decoded_seats == [567]

    day._input_data = ["FFFBBBFRRR"]
    day._preprocess_input()

    assert day._Day__decoded_seats == [119]
    day._input_data = ["BBFFBBFRLL"]
    day._preprocess_input()
    assert day._Day__decoded_seats == [820]


def test_calculate_1():
    day._Day__decoded_seats = [357, 567, 119]
    assert day._calculate_1() == 567


def test_calculate_2():
    day._Day__decoded_seats = [18, 19, 21, 22]
    assert day._calculate_2() == 20
