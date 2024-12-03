# from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2024.day2 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""",
    ),
):
    day = Day()


def test__preprocess_input():
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 2


def test_calculate_2():
    r = day._calculate_2()
    assert r == 4
