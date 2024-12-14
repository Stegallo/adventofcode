# from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2024.day11 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""125 17""",  # noqa: E501
    ),
):
    day = Day()


def test__preprocess_input():
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 55312


def test_calculate_2():
    r = day._calculate_2()
    assert r == 65601038650482
