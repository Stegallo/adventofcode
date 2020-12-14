from unittest.mock import mock_open, patch

from y_2020.day14 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]
    day._preprocess_input()
    assert day._Day__input == [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]


def test_calculate_1():
    print()
    day._Day__input = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]
    assert day._calculate_1() == 165


def test_calculate_2():
    print()
    day._Day__input = [
        "mask = 000000000000000000000000000000X1001X",
        "mem[42] = 100",
        "mask = 00000000000000000000000000000000X0XX",
        "mem[26] = 1",
    ]
    assert day._calculate_2() == 208


def test_calculate_2_short():
    print()
    day._Day__input = [
        "mask = 0X1001X",
        "mem[42] = 100",
        "mask = 000X0XX",
        "mem[26] = 1",
    ]
    assert day._calculate_2() == 208
