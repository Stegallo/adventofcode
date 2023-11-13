from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2015.day10 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test_apply_times():
    assert day._apply_times("1", 1) == "11"
    assert day._apply_times("11", 1) == "21"

    assert day._apply_times("1", 2) == "21"
    assert day._apply_times("1", 3) == "1211"
    assert day._apply_times("1", 4) == "111221"
    assert day._apply_times("1", 5) == "312211"


def test_calculate_1():
    day._Day__input_data = ["1"]
    assert day._calculate_1() == "11"

    day._Day__input_data = ["1", "1"]
    assert day._calculate_1() == "21"

    day._Day__input_data = ["2", "1"]
    assert day._calculate_1() == "1211"

    day._Day__input_data = ["1", "2", "1", "1"]
    assert day._calculate_1() == "111221"

    day._Day__input_data = ["1", "1", "1", "2", "2", "1"]
    assert day._calculate_1() == "312211"


def test_calculate_2():
    day._Day__input_data = ["1"]
    assert day._calculate_2() == 0
