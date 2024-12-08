# from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2024.day7 import Day, Row

with patch(
    "builtins.open",
    mock_open(
        read_data="""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""",  # noqa: E501
    ),
):
    day = Day()


def test__preprocess_input():
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 3749


def test_calculate_2():
    r = day._calculate_2()
    assert r == 11387


def test_row_solve1_True():
    r = Row("190: 10 19")
    assert r.solve1()


def test_row_solve1_False():
    r = Row("83: 17 5")
    assert not r.solve1()


def test_row_solve2_True():
    r = Row("156: 15 6")
    assert r.solve2()


def test_row_solve2_False():
    r = Row("83: 17 5")
    assert not r.solve2()
