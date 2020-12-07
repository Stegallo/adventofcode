from unittest.mock import mock_open, patch

from y_2019.day1 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    day._input_data = [
        "143843",
        "144558",
        "116244",
    ]
    day._preprocess_input()
    assert day._Day__mass_list == [143843, 144558, 116244]

    day._input_data = []
    day._preprocess_input()
    assert day._Day__mass_list == []


def test_calculate_1():
    day._Day__mass_list = [12]
    assert day._calculate_1() == 2


def test_calculate_2():
    day._Day__mass_list = [100756]
    assert day._calculate_2() == 50346


def test_fuel_from_mass():
    assert Day.fuel_from_mass(12) == 2
    assert Day.fuel_from_mass(14) == 2
    assert Day.fuel_from_mass(1969) == 654
    assert Day.fuel_from_mass(100756) == 33583


def test_total_fuel_from_mass():
    assert Day.total_fuel_from_mass(14) == 2
    assert Day.total_fuel_from_mass(1969) == 966
    assert Day.total_fuel_from_mass(100756) == 50346
