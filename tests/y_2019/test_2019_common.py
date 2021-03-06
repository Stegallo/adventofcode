import contextlib
from unittest.mock import patch

from y_2019.common import load_input, main


def test_load_input_string():
    with patch("y_2019.common.open") as open_patch:
        open_patch().__enter__().read = lambda: "hello"
        assert load_input(0) == ["hello"]


def test_load_input_multiline():
    with patch("y_2019.common.open") as open_patch:
        open_patch().__enter__().read = lambda: "hello\nworld\n"
        assert load_input(0) == ["hello", "world"]


def test_main():
    with contextlib.ExitStack() as patches:
        patches.enter_context(patch("y_2019.common.argparse"))
        patches.enter_context(patch("y_2019.common.open"))
        patches.enter_context(patch("y_2019.common.importlib"))
        assert main() is None
