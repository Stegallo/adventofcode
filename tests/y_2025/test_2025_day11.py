# Example + expected answers from the 2025 day 11 puzzle.
# Part 1 and part 2 use different example inputs.
from unittest.mock import mock_open, patch

from y_2025.day11 import Day

# Part 1 example: count paths from "you" to "out".
with patch(
    "builtins.open",
    mock_open(
        read_data="""aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""",
    ),
):
    day_p1 = Day()

# Part 2 example: constrained path counting from "svr".
with patch(
    "builtins.open",
    mock_open(
        read_data="""svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out""",
    ),
):
    day_p2 = Day()


def test__preprocess_input():
    day_p1._preprocess_input()
    day_p2._preprocess_input()
    assert True


def test_calculate_1():
    assert day_p1._calculate_1() == 5


def test_calculate_2():
    assert day_p2._calculate_2() == 2
