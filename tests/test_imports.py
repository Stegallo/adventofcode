"""Smoke test: every solution/common module must import cleanly.

Side benefit: untested solution files then appear in coverage (their import-time
code counts as covered, method bodies as uncovered) instead of being invisible.
"""

from __future__ import annotations

import importlib
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent


def _modules() -> list[str]:
    mods = [f"{p.parent.name}.{p.stem}" for p in ROOT.glob("y_*/day*.py")]
    mods += [
        f"common.{p.stem}"
        for p in (ROOT / "common").glob("*.py")
        if p.stem != "__init__"
    ]
    return sorted(mods)


@pytest.mark.parametrize("module", _modules())
def test_module_imports(module: str) -> None:
    importlib.import_module(module)
