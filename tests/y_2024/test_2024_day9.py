# from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2024.day9 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""2333133121414131402""",  # noqa: E501
    ),
):
    day = Day()


def test__preprocess_input():
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 1928


def test_calculate_2():
    r = day._calculate_2()
    assert r == 2858
