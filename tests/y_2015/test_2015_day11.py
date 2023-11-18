from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2015.day11 import Day, increment_string, increasing, not_iol, pairs

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test_increment_string():
    assert increment_string("a") == "b"
    assert increment_string("xx") == "xy"
    assert increment_string("xy") == "xz"
    assert increment_string("xz") == "ya"
    assert increment_string("ya") == "yb"
    assert increment_string("az") == "ba"
    assert increment_string("azz") == "baa"
    assert increment_string("z") == "aa"
    assert increment_string("zz") == "aaa"


def test_increasing():
    assert increasing("hijklmmn") is True
    assert increasing("abbceffg") is False


def test_not_iol():
    assert not_iol("hijklmmn") is False


def test_pairs():
    assert pairs("abbceffg") is True
    assert pairs("abbcegjk") is False


def test_calculate_1():
    day._Day__input_data = ["a"]
    assert day._calculate_1() == "aabcc"


def test_calculate_2():
    day._Day__input_data = ["a"]
    assert day._calculate_2() == "bbcdd"
