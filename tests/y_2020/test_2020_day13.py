from unittest.mock import mock_open, patch

from y_2020.day13 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = []
    day._preprocess_input()
    assert day._Day__input == []


def test_calculate_1():
    print()
    day._Day__input = ["939", "7,13,x,x,59,x,31,19"]
    assert day._calculate_1() == 295


def test_calculate_2_basic():
    print()
    day._Day__input = ["939", "7,13"]
    assert day._calculate_2() == 77


def test_calculate_2_basic_1():
    print()
    day._Day__input = ["939", "7,13,x,x,59"]
    assert day._calculate_2() == 350


def test_calculate_2_basic_1_bis():
    print()
    day._Day__input = ["939", "17,x,13,19"]
    assert day._calculate_2() == 3417


def test_calculate_2_basic_2():
    print()
    day._Day__input = ["939", "7,13,x,x,59,x,31"]
    assert day._calculate_2() == 70147


def test_calculate_2():
    print()
    day._Day__input = ["939", "7,13,x,x,59,x,31,19"]
    assert day._calculate_2() == 1068781


def test_calculate_2_2():
    print()
    day._Day__input = ["", "17,x,13,19"]
    assert day._calculate_2() == 3417


def test_calculate_2_3():
    print()
    day._Day__input = ["", "67,7,59,61"]
    assert day._calculate_2() == 754018


def test_calculate_2_4():
    print()
    day._Day__input = ["", "67,x,7,59,61"]
    assert day._calculate_2() == 779210


def test_calculate_2_5():
    print()
    day._Day__input = ["", "67,7,x,59,61"]
    assert day._calculate_2() == 1261476


def test_calculate_2_6():
    print()
    day._Day__input = ["", "1789,37,47,1889"]
    assert day._calculate_2() == 1_202_161_486
