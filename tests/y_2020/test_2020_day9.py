from unittest.mock import mock_open, patch

from y_2020.day9 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = [
        "35",
        "20",
        "15",
        "25",
        "47",
        "40",
        "62",
        "55",
        "65",
        "95",
        "102",
        "117",
        "150",
        "182",
        "127",
        "219",
        "299",
        "277",
        "309",
        "576",
    ]
    day._preprocess_input()
    assert day._Day__input == [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]


def test_calculate_1():
    print()
    day._Day__input == [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]
    assert day._calculate_1(5) == 127


def test_calculate_2():
    print()
    day._Day__input == [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]
    assert day._calculate_2(127) == 62
