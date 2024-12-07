# from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2024.day5 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""",  # noqa: E501
    ),
):
    day = Day()


def test__preprocess_input():
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 143


def test_calculate_2():
    r = day._calculate_2()
    assert r == 123
