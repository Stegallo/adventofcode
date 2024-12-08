# from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2024.day4 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""",  # noqa: E501
    ),
):
    day = Day()


def test__preprocess_input():
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 18


def test_calculate_2():
    r = day._calculate_2()
    assert r == 9
