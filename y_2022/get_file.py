import requests

S = requests.Session()
S.headers["User-Agent"] = "github.com/stegallo"
URL = "https://adventofcode.com/{:d}/day/{:d}/{:s}"
YEAR, DAY = 2022, 2
S.cookies.set("session", "")
r = S.get(URL.format(YEAR, DAY, "input"))
r.text
with open("__test_input.txt", "w") as f:
    f.write(r.text)
