from unittest.mock import mock_open, patch

from y_2022.common import load_input
from y_2022.day5 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    day._input_data = [
        [
            "    [D]",
            "[N] [C]",
            "[Z] [M] [P]",
            " 1   2   3",
        ],
        [
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2",
        ],
    ]
    day._preprocess_input()
    assert day._Day__stack == {1: ["[Z]", "[N]"], 2: ["[M]", "[C]", "[D]"], 3: ["[P]"]}
    assert day._Day__max_rack == 3


def test_complete():
    day._input_data = load_input(5, 1)
    day._preprocess_input()
    assert day._calculate_1() == "CMZ"
    assert day._calculate_2() == "MCD"
