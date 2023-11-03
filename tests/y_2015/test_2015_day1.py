from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2015.day1 import Day

with patch("builtins.open", mock_open(read_data="0")):
    day = Day()


def test_calculate_1():
    day._Day__input_data = "(())"
    assert day._calculate_1() == 0

    day._Day__input_data = "((("
    assert day._calculate_1() == 3

    day._Day__input_data = "(()(()("
    assert day._calculate_1() == 3

    day._Day__input_data = "))((((("
    assert day._calculate_1() == 3

    day._Day__input_data = "())"
    assert day._calculate_1() == -1

    day._Day__input_data = "))("
    assert day._calculate_1() == -1

    day._Day__input_data = ")))"
    assert day._calculate_1() == -3

    day._Day__input_data = ")())())"
    assert day._calculate_1() == -3


def test_calculate_2():
    day._Day__input_data = ")"
    assert day._calculate_2() == 1

    day._Day__input_data = "()())"
    assert day._calculate_2() == 5

    day._Day__input_data = "("
    assert day._calculate_2() == -1
