# from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2025.day2 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""",
    ),
):
    day = Day()


def test__preprocess_input():
    day._preprocess_input()
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 1227775554


def test_calculate_2():
    r = day._calculate_2()
    assert r == 4174379265
