from unittest.mock import mock_open, patch

from y_2020.day5 import Day

with patch("builtins.open", mock_open(read_data=":")):
    day = Day()


def test_calculate_1():
    day._input_data = day._preprocess_input(["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR"])
    assert day._calculate_1() == 567


def test_calculate_2():
    day._input_data = [18, 19, 21, 22]
    assert day._calculate_2() == 20


def test_preprocess_input():

    assert day._preprocess_input(["FBFBBFFRLR"]) == [357]
    assert day._preprocess_input(["BFFFBBFRRR"]) == [567]
    assert day._preprocess_input(["FFFBBBFRRR"]) == [119]
    assert day._preprocess_input(["BBFFBBFRLL"]) == [820]
