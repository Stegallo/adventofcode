from __future__ import annotations

from unittest.mock import MagicMock, mock_open, patch

from y_2015.day4 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test_hash_logic():
    day._input_data = [["abcdef"]]
    day._preprocess_input()
    assert day.hash_logic(1) == 31

    day._input_data = [["abcdef"]]
    day._preprocess_input()
    assert day.hash_logic(2) == 298

    day._input_data = [["abcdef"]]
    day._preprocess_input()
    assert day.hash_logic(3) == 3337

    day._input_data = [["abcdef"]]
    day._preprocess_input()
    assert day.hash_logic(4) == 31556


def test_calculate_1():
    day.hash_logic = MagicMock()
    day._calculate_1()
    day.hash_logic.assert_called_once_with(5)


def test_calculate_2():
    day.hash_logic = MagicMock()
    day._calculate_2()
    day.hash_logic.assert_called_once_with(6)
