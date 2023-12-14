from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2023.day13 import Day, Grid

with patch("builtins.open", mock_open(read_data="0")):
    day = Day()


def test_grid():
    print()
    g = Grid(['ab', 'cd'])
    print(g)
    assert g.rows == ['ab', 'cd']
    assert g.cols == ['ac', 'bd']


def test__preprocess_input():
    assert True


def test_calculate_1():
    assert True


def test_calculate_2():
    assert True
