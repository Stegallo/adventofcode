import hashlib


def hash_logic(i: str, num_zeros: int) -> int:
    n = 0
    while True:
        result = hashlib.md5(i.encode("ascii") + str(n).encode("ascii")).hexdigest()
        if result[:num_zeros] == "0" * num_zeros:
            return n
        n += 1


def calculate_1(i: str) -> int:
    return hash_logic(i, 5)


def calculate_2(i: str) -> int:
    return hash_logic(i, 6)
