import hashlib


def calculate_1(i: str) -> int:
    n = 0
    while True:
        result = hashlib.md5(i.encode("ascii") + str(n).encode("ascii")).hexdigest()
        if result[:5] == "00000":
            return n
        n += 1


def calculate_2(i: str) -> int:
    n = 0
    while True:
        result = hashlib.md5(i.encode("ascii") + str(n).encode("ascii")).hexdigest()
        if result[:6] == "000000":
            return n
        n += 1
