import requests

from .secret import SESSION

S = requests.Session()
S.headers["User-Agent"] = "github.com/stegallo"
URL = "https://adventofcode.com/{:d}/day/{:d}/{:s}"
YEAR, DAY = 2022, 2
S.cookies.set("session", SESSION)
r = S.get(URL.format(YEAR, DAY, "input"))
r.text
with open(f"y_{YEAR}/input_day{DAY}.txt", "w") as f:
    f.write(r.text)
