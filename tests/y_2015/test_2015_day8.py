from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2015.day8 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test_calculate_1():
    day._Day__input_data = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']
    assert day._calculate_1() == 12


def test_calculate_2():
    day._Day__input_data = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']
    assert day._calculate_2() == 19
