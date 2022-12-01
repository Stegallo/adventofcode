import contextlib
from unittest.mock import patch

from y_2022.common import AoCDay, load_input, main


def test_load_input_string():
    with patch("y_2022.common.open") as open_patch:
        open_patch().__enter__().read = lambda: "hello"
        assert load_input(0, 0) == [["hello"]]
        open_patch().__enter__().read = lambda: ""
        assert load_input(0, 0) == [[""]]


def test_load_input_multiline():
    with patch("y_2022.common.open") as open_patch:
        open_patch().__enter__().read = lambda: "hello\nworld\n"
        assert load_input(0, 0) == [["hello", "world"]]


def test_load_input_multiline_multisection():
    with patch("y_2022.common.open") as open_patch:
        open_patch().__enter__().read = (
            lambda: "hello\nworld\n\ngoodbye\nworld\n\nbye\n"
        )
        assert load_input(0, 0) == [["hello", "world"], ["goodbye", "world"], ["bye"]]


def test_main():
    with contextlib.ExitStack() as patches:
        patches.enter_context(patch("y_2022.common.argparse"))
        patches.enter_context(patch("y_2022.common.open"))
        patches.enter_context(patch("y_2022.common.importlib"))
        assert main() is None


class MockAoCDay(AoCDay):
    def __init__(self):
        super().__init__(0, 0)

    def _calculate_1(self):
        pass

    def _calculate_2(self):
        pass

    def _preprocess_input(self):
        pass


def test_AoCDay():
    print()
    with patch("y_2022.common.open") as open_patch:
        open_patch().__enter__().read = lambda: "hello\nworld\n"
        mock_aoc_day = MockAoCDay()
    assert mock_aoc_day.solve() is None
