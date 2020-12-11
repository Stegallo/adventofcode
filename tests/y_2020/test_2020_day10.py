from unittest.mock import mock_open, patch

from y_2020.day10 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    day._preprocess_input()
    assert day._Day__input == [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]


def test_calculate_1():
    print()
    day._Day__input = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    assert day._calculate_1() == 7 * 5
    day._Day__input = [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]
    assert day._calculate_1() == 22 * 10


def test_calculate_2():
    print()
    day._Day__input = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    assert day._calculate_2() == 8
    day._Day__input = [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]
    assert day._calculate_2() == 19208
