from y_2015.day6 import calculate_1, calculate_2, parse, defaultdict
from unittest.mock import patch


def test_parse():
    assert parse("turn on 0,0 through 999,999") == (
        "turn on",
        (0, 0),
        "through",
        (999, 999),
    )
    assert parse("toggle 0,0 through 999,0") == ("toggle", (0, 0), "through", (999, 0))


def test_calculate_1_all_off_turn_on():
    with patch("y_2015.day6.GRID", defaultdict(int)):
        assert calculate_1(["turn on 0,0 through 999,999"]) == 1000000


def test_calculate_1_all_on_toggle():
    with patch("y_2015.day6.GRID", defaultdict(int)):
        assert calculate_1(["toggle 0,0 through 999,0"]) == 1000


def test_calculate_1_all_on_turn_off():
    with patch("y_2015.day6.GRID", defaultdict(int)):
        assert calculate_1(["turn off 499,499 through 500,500"]) == 0


def test_calculate_2_first():
    with patch("y_2015.day6.GRID", defaultdict(int)):
        assert calculate_2(["turn on 0,0 through 0,0"]) == 1


def test_calculate_2_second():
    with patch("y_2015.day6.GRID", defaultdict(int)):
        assert calculate_2(["toggle 0,0 through 999,999"]) == 2000000
