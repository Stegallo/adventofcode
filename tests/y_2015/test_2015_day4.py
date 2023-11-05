from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2015.day4 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test_calculate_1():
    day._input_data = [["abcdef"]]
    day._preprocess_input()
    assert day._calculate_1() == 609043

    day._input_data = [["pqrstuv"]]
    day._preprocess_input()
    assert day._calculate_1() == 1048970
