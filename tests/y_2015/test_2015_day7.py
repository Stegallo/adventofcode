from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2015.day7 import Day, Element

with patch(
    "builtins.open",
    mock_open(
        read_data="""123 -> x\n"""
        """456 -> y\n"""
        """x AND y -> d\n"""
        """x OR y -> e\n"""
        """x LSHIFT 2 -> f\n"""
        """y RSHIFT 2 -> g\n"""
        """NOT x -> h\n"""
        """NOT y -> i\n"""
        """x -> a""",
    ),
):
    day = Day()


def test_calculate_1():
    assert day._calculate_1() == 123


def test_calculate_2():
    assert day._calculate_2() == 123


def test_Element_resolve():
    element = Element("123")
    assert element.resolve({}) == 123

    element = Element("a")
    assert element.resolve({"a": Element("1")}) == 1

    element = Element("NOT 1")
    assert element.resolve({}) == 65534

    element = Element("a")
    assert element.resolve({"a": Element("b AND b"), "b": Element("1")}) == 1
