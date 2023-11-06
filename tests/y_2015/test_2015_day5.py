from __future__ import annotations

from unittest.mock import mock_open, patch

from pydantic.dataclasses import dataclass

from y_2015.day5 import Day, NiceString

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test_NiceString__has_3_vovels():
    assert NiceString("")._NiceString__has_3_vovels() is False
    assert NiceString("a")._NiceString__has_3_vovels() is False
    assert NiceString("aa")._NiceString__has_3_vovels() is False
    assert NiceString("aab")._NiceString__has_3_vovels() is False
    assert NiceString("aaa")._NiceString__has_3_vovels() is True

    assert NiceString("ugknbfddgicrmopn")._NiceString__has_3_vovels() is True
    assert NiceString("aaa")._NiceString__has_3_vovels() is True
    assert NiceString("dvszwmarrgswjxmb")._NiceString__has_3_vovels() is False


def test_NiceString__has_one_letter_twice():
    assert NiceString("")._NiceString__has_one_letter_twice() is False
    assert NiceString("a")._NiceString__has_one_letter_twice() is False
    assert NiceString("aa")._NiceString__has_one_letter_twice() is True
    assert NiceString("aba")._NiceString__has_one_letter_twice() is False
    assert NiceString("abaa")._NiceString__has_one_letter_twice() is True

    assert NiceString("ugknbfddgicrmopn")._NiceString__has_one_letter_twice() is True
    assert NiceString("aaa")._NiceString__has_one_letter_twice() is True
    assert NiceString("jchzalrnumimnmhp")._NiceString__has_one_letter_twice() is False


def test_NiceString__has_no_forbidden_pairs():
    assert NiceString("")._NiceString__has_no_forbidden_pairs() is True
    assert NiceString("ab")._NiceString__has_no_forbidden_pairs() is False
    assert NiceString("cd")._NiceString__has_no_forbidden_pairs() is False
    assert NiceString("pq")._NiceString__has_no_forbidden_pairs() is False
    assert NiceString("xy")._NiceString__has_no_forbidden_pairs() is False
    assert NiceString("acpx")._NiceString__has_no_forbidden_pairs() is True

    assert NiceString("ugknbfddgicrmopn")._NiceString__has_no_forbidden_pairs() is True
    assert NiceString("aaa")._NiceString__has_no_forbidden_pairs() is True
    assert NiceString("haegwjzuvuyypxyu")._NiceString__has_no_forbidden_pairs() is False


def test_NiceString_nice():
    assert NiceString("ugknbfddgicrmopn").nice is True
    assert NiceString("aaa").nice is True
    assert NiceString("jchzalrnumimnmhp").nice is False
    assert NiceString("haegwjzuvuyypxyu").nice is False
    assert NiceString("dvszwmarrgswjxmb").nice is False


def test_NiceString__has_pair_twice():
    assert NiceString("xyxy")._NiceString__has_pair_twice() is True
    assert NiceString("aabcdefgaa")._NiceString__has_pair_twice() is True
    assert NiceString("aaa")._NiceString__has_pair_twice() is False

    assert NiceString("qjhvhtzxzqqjkmpb")._NiceString__has_pair_twice() is True
    assert NiceString("xxyxx")._NiceString__has_pair_twice() is True
    assert NiceString("ieodomkazucvgmuy")._NiceString__has_pair_twice() is False


def test_NiceString__has_letter_repeats_with_one_between():
    assert NiceString("xyx")._NiceString__has_letter_repeats_with_one_between() is True
    assert (
        NiceString("abcdefeghi")._NiceString__has_letter_repeats_with_one_between()
        is True
    )
    assert NiceString("aaa")._NiceString__has_letter_repeats_with_one_between() is True

    assert (
        NiceString(
            "qjhvhtzxzqqjkmpb",
        )._NiceString__has_letter_repeats_with_one_between()
        is True
    )
    assert (
        NiceString("xxyxx")._NiceString__has_letter_repeats_with_one_between() is True
    )
    assert (
        NiceString(
            "uurcxstgmygtbstg",
        )._NiceString__has_letter_repeats_with_one_between()
        is False
    )


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
