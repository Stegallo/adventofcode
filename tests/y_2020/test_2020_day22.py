from unittest.mock import mock_open, patch
from collections import deque
from y_2020.day22 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = [
        "Player 1:",
        "9",
        "2",
        "6",
        "3",
        "1",
        "",
        "Player 2:",
        "5",
        "8",
        "4",
        "7",
        "10",
    ]
    day._preprocess_input()
    assert day._Day__p1 == deque([9, 2, 6, 3, 1])
    assert day._Day__p2 == deque([5, 8, 4, 7, 10])


def test__play_round():
    print()
    day._Day__p1 = deque([9, 2, 6, 3, 1])
    day._Day__p2 = deque([5, 8, 4, 7, 10])
    day._Day__play_round(1)
    assert day._Day__p1 == deque([2, 6, 3, 1, 9, 5])
    assert day._Day__p2 == deque([8, 4, 7, 10])

    day._Day__p1 = deque([2, 6, 3, 1, 9, 5])
    day._Day__p2 = deque([8, 4, 7, 10])
    day._Day__play_round(2)
    assert day._Day__p1 == deque([6, 3, 1, 9, 5])
    assert day._Day__p2 == deque([4, 7, 10, 8, 2])


def test_calculate_1():
    print()
    day._input_data = [
        "Player 1:",
        "9",
        "2",
        "6",
        "3",
        "1",
        "",
        "Player 2:",
        "5",
        "8",
        "4",
        "7",
        "10",
    ]
    day._preprocess_input()
    assert day._calculate_1() == 306


def test_calculate_2():
    print()
    day._input_data = []
    day._preprocess_input()
    assert day._calculate_2() == 0
