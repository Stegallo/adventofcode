# Example + expected answers from the 2025 day 8 puzzle.
from unittest.mock import mock_open, patch

from y_2025.day08 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""",
    ),
):
    day = Day(test=1)  # test flag -> 10 connections for the example (real: 1000)


def test__preprocess_input():
    day._preprocess_input()
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 40


def test_calculate_2():
    r = day._calculate_2()
    assert r == 25272
