import contextlib
from unittest.mock import patch

from common.aoc import AoCDay, main


def test_load_input_string():
    with patch("common.aoc.open") as open_patch:
        AoCDay.__abstractmethods__=set()
        aoc_day = AoCDay('y_1900.day1', False)

        open_patch().__enter__().read = lambda: "hello"
        assert aoc_day._load_input() == [["hello"]]
        open_patch().__enter__().read = lambda: ""
        assert aoc_day._load_input() == [[""]]


def test_load_input_multiline():
    with patch("common.aoc.open") as open_patch:
        AoCDay.__abstractmethods__=set()
        aoc_day = AoCDay('y_1900.day1', False)

        open_patch().__enter__().read = lambda: "hello\nworld\n"
        assert aoc_day._load_input() == [["hello", "world"]]


def test_load_input_multiline_multisection():
    with patch("common.aoc.open") as open_patch:
        AoCDay.__abstractmethods__=set()
        aoc_day = AoCDay('y_1900.day1', False)

        open_patch().__enter__().read = (
            lambda: "hello\nworld\n\ngoodbye\nworld\n\nbye\n"
        )
        assert aoc_day._load_input() == [["hello", "world"], ["goodbye", "world"], ["bye"]]


def test_main():
    with contextlib.ExitStack() as patches:
        patches.enter_context(patch("common.aoc.argparse"))
        patches.enter_context(patch("common.aoc.open"))
        patches.enter_context(patch("common.aoc.importlib"))
        assert main() is None


def test_AoCDay():
    with patch("common.aoc.open") as open_patch:
        AoCDay.__abstractmethods__=set()
        aoc_day = AoCDay('y_1900.day1', False)
        open_patch().__enter__().read = lambda: "hello\nworld\n"
    assert aoc_day.solve() is None
