from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2015.day3 import Day

with patch("builtins.open", mock_open(read_data="1x1x1")):
    day = Day()


def test_calculate_1():
    day._input_data = [[">"]]
    day._preprocess_input()
    assert day._calculate_1() == 2

    day._input_data = [["^>v<"]]
    day._preprocess_input()
    assert day._calculate_1() == 4

    day._input_data = [["^v^v^v^v^v"]]
    day._preprocess_input()
    assert day._calculate_1() == 2


def test_calculate_2():
    day._input_data = [["^v"]]
    day._preprocess_input()
    assert day._calculate_2() == 3

    day._input_data = [["^>v<"]]
    day._preprocess_input()
    assert day._calculate_2() == 3

    day._input_data = [["^v^v^v^v^v"]]
    day._preprocess_input()
    assert day._calculate_2() == 11
