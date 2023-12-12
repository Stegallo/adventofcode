from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2023.day5 import Day, SeedRange

with patch("builtins.open", mock_open(read_data="seeds: 79 14 55 13")):
    day = Day()


def test_SeedRange_split():
    print()
    sr = SeedRange(5, 10)
    n_sr = sr.split(6, 9)
    print(n_sr)
    assert n_sr == [SeedRange(5, 5), SeedRange(6, 9), SeedRange(10, 10)]
    n_sr = sr.split(4, 11)
    print(n_sr)
    assert n_sr == [SeedRange(5, 10)]
    n_sr = sr.split(4, 9)
    print(n_sr)
    assert n_sr == [SeedRange(5, 9), SeedRange(10, 10)]
    n_sr = sr.split(6, 11)
    print(n_sr)
    assert n_sr == [SeedRange(5, 5), SeedRange(6, 10)]

    sr = SeedRange(79, 93)
    n_sr = sr.split(98, 99)
    print(n_sr)
    assert n_sr == [SeedRange(79, 93)]

    sr = SeedRange(81, 95)
    n_sr = sr.split(25, 94)
    print(n_sr)
    assert n_sr == [SeedRange(81, 94), SeedRange(95, 95)]


def test__preprocess_input():
    pass


def test_calculate_1():
    pass


def test_calculate_2():
    pass
