from __future__ import annotations

import requests

from secret import SESSION


def pull_file(year:str, day: str):
    S = requests.Session()
    S.headers["User-Agent"] = "github.com/stegallo"
    URL = "https://adventofcode.com/{:d}/day/{:d}/{:s}"
    YEAR, DAY = int(year), int(day)
    S.cookies.set("session", SESSION)
    r = S.get(URL.format(YEAR, DAY, "input"))
    with open(f"y_{YEAR}/input_day{DAY}.txt", "w") as f:
        f.write(r.text)
