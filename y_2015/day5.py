from collections import defaultdict
from typing import DefaultDict


def calculate_1(i: str) -> int:
    vowels_count = 0
    twice = False
    contains_bad_string = False
    for l in i:
        if l in ["a", "e", "i", "o", "u"]:
            vowels_count += 1
    for j, l in enumerate(i):
        if j == 0:
            continue
        if i[j - 1] == l:
            twice = True
        if i[j - 1] + l in ["ab", "cd", "pq", "xy"]:
            contains_bad_string = True
    return int(vowels_count >= 3 and twice and not contains_bad_string)


def twiced(i: str) -> bool:
    pairs: DefaultDict[tuple, int] = defaultdict(int)
    twice = False
    for j, l in enumerate(i):
        if j == 0:
            continue

        if j <= 1:
            pairs[(i[j - 1], l)] += 1
            continue

        if not (i[j - 2] == i[j - 1] and i[j - 1] == i[j]) or (
            j > 2 and i[j - 3] == i[j - 2]
        ):
            pairs[(i[j - 1], l)] += 1

    for j in pairs:
        if pairs[j] > 1:
            twice = True
    return twice


def repeated(i: str) -> int:
    for j, l in enumerate(i):
        if j <= 1:
            continue
        if i[j - 2] == l:
            return True
    return False


def calculate_2(i: str) -> int:
    twice = twiced(i)
    repeat = repeated(i)
    return int(twice and repeat)
