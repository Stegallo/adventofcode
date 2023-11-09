from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2015.day7 import Day, Ingress

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


def test_ingress_resolve():
    ingress = Ingress("123")
    assert ingress.resolve({}) == Ingress("123")

    ingress = Ingress("a")
    assert ingress.resolve({"a": Ingress("1")}) == Ingress("1")

    ingress = Ingress("NOT 1")
    assert ingress.resolve({}) == Ingress("65534")

    ingress = Ingress("NOT a")
    assert ingress.resolve({"a": Ingress("1")}) == Ingress("65534")

    ingress = Ingress("x AND y")
    assert ingress.resolve({"x": Ingress("123"), "y": Ingress("456")}) == Ingress("72")

    ingress = Ingress("x OR y")
    assert ingress.resolve({"x": Ingress("123"), "y": Ingress("456")}) == Ingress("507")

    ingress = Ingress("x LSHIFT 2")
    assert ingress.resolve({"x": Ingress("123")}) == Ingress("492")

    ingress = Ingress("y RSHIFT 2")
    assert ingress.resolve({"y": Ingress("456")}) == Ingress("114")
