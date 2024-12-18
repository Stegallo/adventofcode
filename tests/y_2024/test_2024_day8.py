# from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2024.day8 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""",  # noqa: E501
    ),
):
    day = Day()


def test__preprocess_input():
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 14


def test_calculate_2():
    r = day._calculate_2()
    assert r == 34
