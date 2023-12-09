from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2023.day3 import Day, Number, extract_numbers

with patch("builtins.open", mock_open(read_data="0")):
    day = Day()


def test_extract_numbers():
    print()
    res = extract_numbers("467..114..", 0)
    print(f"{res=}")
    assert res == [
        Number(467, 0, 0, 3),
        Number(114, 0, 5, 3),
    ]
    assert extract_numbers("467", 0) == [Number(467, 0, 0, 3)]
    # assert False


def test__preprocess_input():
    assert True


def test_calculate_1():
    assert True


def test_calculate_2():
    assert True
