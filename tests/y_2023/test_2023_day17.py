from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2023.day17 import Day, Grid, Cru,DOWN,UP,LEFT,RIGH


with patch("builtins.open", mock_open(read_data="0")):
    day = Day()


def test_cru():
    print()
    # 24
    # 32
    g = Grid(['24', '32'])
    print(g)
    c = Cru(g, (0,0), DOWN, 0)

    assert c.neib == {
        Cru(g, (0,1), DOWN, 1),
        Cru(g, (1,0), RIGH, 0),}

    assert c.neib_cost == {
        (Cru(g, (0,1), DOWN, 1), 3),
        (Cru(g, (1,0), RIGH, 0), 4),}


    c = Cru(g, (1,1), DOWN, 0)
    assert c.neib == {
        Cru(g, (0,1), LEFT, 0),}

    assert c.neib_cost == {
        (Cru(g, (0,1), LEFT, 0), 3),}


def test__preprocess_input():
    assert True


def test_calculate_1():
    assert True


def test_calculate_2():
    assert True
