# from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2024.day1 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""3   4
4   3
2   5
1   3
3   9
3   3""",
    ),
):
    day = Day()


def test__preprocess_input():
    day._preprocess_input()
    assert day._Day__first_list == [3, 4, 2, 1, 3, 3]
    assert day._Day__second_list == [4, 3, 5, 3, 9, 3]


def test_calculate_1():
    r = day._calculate_1()
    assert r == 11


def test_calculate_2():
    r = day._calculate_2()
    assert r == 31
