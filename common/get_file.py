from __future__ import annotations

import os

import requests


def _session_cookie() -> str:
    """AoC session cookie, from $AOC_SESSION or a local (git-ignored) secret.py."""
    token = os.environ.get("AOC_SESSION")
    if token:
        return token
    try:
        from secret import SESSION

        return SESSION
    except ImportError:
        return ""


def pull_file(year: str, day: str):
    S = requests.Session()
    S.headers["User-Agent"] = "github.com/stegallo"
    URL = "https://adventofcode.com/{:d}/day/{:d}/{:s}"
    YEAR, DAY = int(year), int(day)
    S.cookies.set("session", _session_cookie())
    r = S.get(URL.format(YEAR, DAY, "input"))
    with open(f"y_{YEAR}/input_day{DAY}.txt", "w") as f:
        f.write(r.text)
