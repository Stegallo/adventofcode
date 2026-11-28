# AGENTS.md

Guidance for AI agents working in this repository.

## Project overview

Personal [Advent of Code](https://adventofcode.com) solutions in Python. Each
year lives in a `y_<year>/` directory (e.g. `y_2015`, `y_2023`, `y_2024`,
`y_2025`) with one file per day (`dayN.py`). Shared infrastructure lives in
`common/`. Tests mirror the solution layout under `tests/`.

A companion Rust repo holds Rust solutions (linked from the README).

## Layout

- `y_1900/day0.py` — the generic starter template (copy it to begin a new day).
  Do **not** commit a per-year `day0.py`; it only lives in `y_1900`.
- `y_<year>/dayN.py` — solution for a given day. Defines a `Day(AoCDay)` class.
- `y_<year>/input_dayN.txt` — real puzzle input (git-ignored, auto-downloaded).
- `y_<year>/input_dayN_test.txt` — optional sample input (used when `test=1`).
- `common/aoc.py` — `AoCDay` abstract base class, `main()` CLI entry, `StopWatch`.
- `common/get_file.py` — downloads puzzle input via the AoC session cookie.
- `common/grid.py` — `Grid`, `Point`, `Cursor`, `Direction`, `DIRS`, `DIRS_8` helpers.
- `common/utilities.py` — misc helpers (bit ops, another `Grid`, etc.).
- `src/__main__.py` — thin wrapper calling `common.aoc.main()`.
- `secret.py` — holds the AoC `SESSION` cookie (needed to fetch inputs).
- `tests/y_<year>/test_<year>_dayN.py` — pytest tests, mock input via `mock_open`.

## Solution pattern

Each `dayN.py` subclasses `AoCDay` and implements four methods:

```python
from common.aoc import AoCDay

class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # parse self._input_data (list of chunks, each a list of lines)
        ...

    def _calculate_1(self):
        ...   # return part 1 answer

    def _calculate_2(self):
        ...   # return part 2 answer
```

`_load_input()` reads the input file, strips a trailing newline, splits on
blank lines (`\n\n`) into chunks, and splits each chunk into lines. So
`self._input_data` is `List[List[str]]`.

The base `__init__` resolves year/day from `__name__` (e.g. `y_2025.day09`), so
always pass `__name__` to `super().__init__`.

## Environment

This project uses [uv](https://docs.astral.sh/uv/) with Python 3.15 (pinned in
`.python-version`). All dependencies and tool config live in `pyproject.toml`;
`uv.lock` is the lockfile. There is no `requirements/` dir or `setup.cfg`.

```bash
uv sync --dev          # create .venv and install runtime + dev deps
uv run <cmd>           # run a command inside the project env
```

## Running a solution

From the repo root (uses the module CLI in `common/aoc.py`):

```bash
uv run python -m src --year 2025 --day 9 --test 0
```

`--test 1` loads `input_dayN_test.txt`; `--test 0` loads the real `input_dayN.txt`.
If the real input is missing, it is auto-downloaded via `common/get_file.py`
(requires a valid `SESSION` in `secret.py`).

## Tests

Run all tests with coverage (matches CI):

```bash
uv run pytest --cov-report term --cov .
```

Run one day's tests:

```bash
uv run pytest tests/y_2025/test_2025_day01.py
```

Tests patch `builtins.open` with `mock_open(read_data=...)` to inject sample
input, then assert on `_calculate_1()` / `_calculate_2()` return values.

## Linting / formatting

Pre-commit runs black, ruff (lint + import sorting), add-trailing-comma, and mypy.

```bash
uv run pre-commit run --all-files   # run every hook
uv run ruff check .                 # lint (CI runs this)
uv run ruff check --fix .           # lint + autofix
uv run black .                      # format
```

- Line length: 88 (ruff config in `pyproject.toml`). Ruff selects `E,F,W,I`
  and ignores `E203,E741,W605`. The `I` rule does import sorting (replaces isort).
- Code style: black. Keep double quotes.
- Ruff replaced flake8 (flake8's pinned pyflakes broke under Python 3.14;
  ruff is a standalone binary unaffected by it).

## Conventions & notes

- Solution files are often full of commented-out scratch/exploration code — this
  is the author's working style. When adding a new day, keep the four-method
  structure but you don't need to preserve scratch comments.
- The private attribute `self.__input_data` (name-mangled per subclass) is the
  common place to store preprocessed data within a `Day`.
- `common/grid.py` uses pydantic dataclasses; a comment notes disabling pydantic
  can be ~5x faster if performance matters.
- `secret.py` contains a session cookie. Do not commit changes that leak or
  alter it unintentionally; it is required only for downloading inputs.
- The README has a progress table with per-day links; new completed days get a
  `[puzzle]` + `[✓]` entry plus matching link references at the bottom.

## CI

GitHub Actions (`.github/workflows/ci.yml`) runs ruff + pytest with coverage
(via `uv`) on push and PRs, and uploads to codecov. A second workflow
(`.github/workflows/black.yml`) opens an auto-format PR after pushes to master.
mypy is enforced via pre-commit (not yet in CI).
