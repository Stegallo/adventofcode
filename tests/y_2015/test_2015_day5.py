from __future__ import annotations

from unittest.mock import mock_open, patch

from pydantic.dataclasses import dataclass

from y_2015.day5 import Day, NiceString

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test_NiceString_nice():
    assert NiceString("ugknbfddgicrmopn").nice is True
    assert NiceString("aaa").nice is True
    assert NiceString("jchzalrnumimnmhp").nice is False
    assert NiceString("haegwjzuvuyypxyu").nice is False
    assert NiceString("dvszwmarrgswjxmb").nice is False


def test_NiceString_correct_nice():
    assert NiceString("qjhvhtzxzqqjkmpb").correct_nice is True
    assert NiceString("xxyxx").correct_nice is True
    assert NiceString("aaaa").correct_nice is True
    assert NiceString("uurcxstgmygtbstg").correct_nice is False
    assert NiceString("ieodomkazucvgmuy").correct_nice is False


def test_calculate_1():
    @dataclass
    class MockNiceString:
        nice: bool

    day._Day__input_data = []
    assert day._calculate_1() == 0

    day._Day__input_data = [MockNiceString(True)]
    assert day._calculate_1() == 1

    day._Day__input_data = [MockNiceString(True), MockNiceString(False)]
    assert day._calculate_1() == 1

    day._Day__input_data = [MockNiceString(True), MockNiceString(True)]
    assert day._calculate_1() == 2

    day._Day__input_data = [
        MockNiceString(True),
        MockNiceString(True),
        MockNiceString(False),
        MockNiceString(False),
    ]
    assert day._calculate_1() == 2


def test_calculate_2():
    @dataclass
    class MockNiceString:
        correct_nice: bool

    day._Day__input_data = [MockNiceString(True), MockNiceString(False)]
    assert day._calculate_2() == 1