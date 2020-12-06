from unittest.mock import mock_open, patch

from y_2020.day6 import Counter, Day, UserGroup

with patch("builtins.open", mock_open(read_data=":")):
    day = Day()


def test__preprocess_input():
    day._input_data = [
        "abc",
        "",
        "a",
        "b",
        "c",
        "",
        "ab",
        "ac",
        "",
        "a",
        "a",
        "a",
        "a",
        "",
        "b",
    ]
    day._preprocess_input()
    assert day._Day__user_groups == [
        UserGroup(answers=Counter({"a": 1, "b": 1, "c": 1}), size=1),
        UserGroup(answers=Counter({"a": 1, "b": 1, "c": 1}), size=3),
        UserGroup(answers=Counter({"a": 2, "b": 1, "c": 1}), size=2),
        UserGroup(answers=Counter({"a": 4}), size=4),
        UserGroup(answers=Counter({"b": 1}), size=1),
    ]


def test_calculate_1():
    day._Day__user_groups = [
        UserGroup(answers=Counter({"a": 1, "b": 1, "c": 1}), size=1),
        UserGroup(answers=Counter({"a": 1, "b": 1, "c": 1}), size=3),
        UserGroup(answers=Counter({"a": 2, "b": 1, "c": 1}), size=2),
        UserGroup(answers=Counter({"a": 4}), size=4),
        UserGroup(answers=Counter({"b": 1}), size=1),
    ]
    assert day._calculate_1() == 11


def test_calculate_2():
    day._Day__user_groups = [
        UserGroup(answers=Counter({"a": 1, "b": 1, "c": 1}), size=1),
        UserGroup(answers=Counter({"a": 1, "b": 1, "c": 1}), size=3),
        UserGroup(answers=Counter({"a": 2, "b": 1, "c": 1}), size=2),
        UserGroup(answers=Counter({"a": 4}), size=4),
        UserGroup(answers=Counter({"b": 1}), size=1),
    ]
    assert day._calculate_2() == 6
