from typing import List


def decimal_from_binary(binary: List) -> int:
    result = 0
    for digit in binary:
        result = result * 2 + digit
    return result
