from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2023.day12 import Day, generate_possible, Row

with patch("builtins.open", mock_open(read_data=". 0")):
    day = Day()


def test_generate_possible():
    assert generate_possible("?") == [".", "#"]
    assert generate_possible("??") == ["..", ".#", "#.", "##"]
    assert generate_possible("???") == [
        "...",
        "..#",
        ".#.",
        ".##",
        "#..",
        "#.#",
        "##.",
        "###",
    ]
    assert generate_possible(".?") == ["..", ".#"]


def test_row_solve_():
    print()
    # return
    r = Row("???.### 1,1,3")
    print(r)
    assert r.solve() == 1

    r = Row(".??..??...?##. 1,1,3")
    print(r)
    assert r.solve() == 4

    r = Row("?#?#?#?#?#?#?#? 1,3,1,6")
    print(r)
    assert r.solve() == 1

    r = Row("????.#...#... 4,1,1")
    print(r)
    assert r.solve() == 1

    r = Row("????.######..#####. 1,6,5")
    print(r)
    assert r.solve() == 4

    r = Row("? 1")
    print(r)
    assert r.solve() == 1

    r = Row("? 2")
    print(r)
    assert r.solve() == 0

    r = Row("?? 1")
    print(r)
    assert r.solve() == 2

    r = Row("??? 1")
    print(r)
    assert r.solve() == 3

    r = Row("???? 1")
    print(r)
    assert r.solve() == 4

    r = Row("?? 2")
    print(r)
    assert r.solve() == 1

    r = Row("#?? 2")
    print(r)
    assert r.solve() == 1

    r = Row("??? 2")
    print(r)
    assert r.solve() == 2


def test_row_solve():
    print()
    r = Row("??? 2")
    print(r)
    assert r.solve() == 2

    r = Row("???? 2")
    print(r)
    assert r.solve() == 3

    r = Row("# 1")
    print(r)
    assert r.solve() == 1

    r = Row("#.# 1,1")
    print(r)
    assert r.solve() == 1

    r = Row("#?# 1,1")
    print(r)
    assert r.solve() == 1

    r = Row("??????? 2,1")
    print(r)
    assert r.solve() == 10

    r = Row("?###???????? 3,2,1")
    print(r)
    assert r.solve() == 10

    r = Row("????.##???????????.? 3,10,1,1")
    print(r)
    assert r.solve() == 4

    r = Row("?..??#????#???#?### 11,3")
    print(r)
    assert r.solve() == 1

    r = Row("?#????##??#?????#?. 1,12")
    print(r)
    assert r.solve() == 2


def test__preprocess_input():
    assert True


def test_calculate_1():
    assert True


def test_calculate_2():
    assert True
