# from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2024.day15 import Day

with patch(
    "builtins.open",
    mock_open(
        read_data="""p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""",  # noqa: E501
    ),
):
    day = Day(test=1)


def test__preprocess_input():
    assert True


def test_calculate_1():
    r = day._calculate_1()
    assert r == 12


def test_calculate_2():
    # r = day._calculate_2()
    assert True
