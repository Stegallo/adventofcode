from unittest.mock import mock_open, patch

from y_2020.day19 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = []
    day._preprocess_input()
    assert day._Day__input == []


def test_calculate_1():
    print()

    day._Day__input = [
        "0: 4 1 5",
        "1: 2 3",
        "2: 4 4",
        "3: 4 5",
        '4: "a"',
        '5: "b"',
        "",
        "aaaabb",
        "aaaabb",
    ]
    assert day._calculate_1() == 2

    day._Day__input = [
        "0: 4 1 5",
        "1: 2 3 | 3 2",
        "2: 4 4 | 5 5",
        "3: 4 5 | 5 4",
        '4: "a"',
        '5: "b"',
        "",
        "ababbb",
        "bababa",
        "abbbab",
        "aaabbb",
        "aaaabbb",
    ]
    assert day._calculate_1() == 2


def test_calculate_2():
    print()
    day._Day__input = []
    assert day._calculate_2() == 0
