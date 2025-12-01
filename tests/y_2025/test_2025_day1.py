# from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2025.day1 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""",
    ),
):
    day = Day()


def test__preprocess_input():
    day._preprocess_input()
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 3


def test_calculate_2():
    r = day._calculate_2()
    assert r == 6


def test_dial_right_wraps():
    dial = 95
    dial = (dial + 10) % 100
    assert dial == 5


def test_dial_left_wraps():
    dial = 5
    dial = (dial - 10) % 100
    assert dial == 95
