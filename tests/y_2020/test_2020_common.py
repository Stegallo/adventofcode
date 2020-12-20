import contextlib
from unittest.mock import patch

from y_2020.common import AoCDay, load_input, main


def test_load_input_string():
    with patch("y_2020.common.open") as open_patch:
        open_patch().__enter__().read = lambda: "hello"
        assert load_input(0) == ["hello"]


def test_load_input_multiline():
    with patch("y_2020.common.open") as open_patch:
        open_patch().__enter__().read = lambda: "hello\nworld\n"
        assert load_input(0) == ["hello", "world"]


def test_main():
    with contextlib.ExitStack() as patches:
        patches.enter_context(patch("y_2020.common.argparse"))
        patches.enter_context(patch("y_2020.common.open"))
        patches.enter_context(patch("y_2020.common.importlib"))
        assert main() is None


class MockAoCDay(AoCDay):
    def __init__(self):
        super().__init__(0)

    def _calculate_1(self):
        pass

    def _calculate_2(self):
        pass

    def _preprocess_input(self):
        pass


def test_AoCDay():
    print()
    with patch("y_2020.common.open") as open_patch:
        open_patch().__enter__().read = lambda: "hello\nworld\n"
        mock_aoc_day = MockAoCDay()
    assert mock_aoc_day.solve() is None
