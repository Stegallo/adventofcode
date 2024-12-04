# from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2024.day3 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))""",
    ),
):
    day = Day()


def test__preprocess_input():
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 161


def test_calculate_2():
    r = day._calculate_2()
    assert r == 48
