# from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2024.day10 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""",  # noqa: E501
    ),
):
    day = Day()


def test__preprocess_input():
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 36


def test_calculate_2():
    r = day._calculate_2()
    assert r == 81
