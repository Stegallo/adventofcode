from unittest.mock import mock_open, patch

from y_2020.day12 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = [
        "F10",
        "N3",
        "F7",
        "R90",
        "F11",
    ]

    day._preprocess_input()
    assert day._Day__input == [
        ("F", 10),
        ("N", 3),
        ("F", 7),
        ("R", 90),
        ("F", 11),
    ]


def test_calculate_1():
    print()
    day._Day__input = [
        ("F", 10),
        ("N", 3),
        ("F", 7),
        ("R", 90),
        ("F", 11),
    ]
    assert day._calculate_1() == 25


def test_calculate_2():
    print()
    day._Day__input = [
        ("F", 10),
        ("N", 3),
        ("F", 7),
        ("R", 90),
        ("F", 11),
    ]
    assert day._calculate_2() == 286


def test_calculate_2_bis():
    print()
    day._Day__input = [
        ("F", 10),
        ("N", 3),
        ("F", 7),
        ("R", 90),
        ("F", 11),
        ("L", 90),
    ]
    assert day._calculate_2() == 286
