from unittest.mock import mock_open, patch

from y_2020.day19 import Day

with patch("builtins.open", mock_open(read_data="0: 0")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = ["0: 0", "", "a"]
    day._preprocess_input()
    assert day._Day__rules == {"0": '0 "c"'}
    assert day._Day__messages == ["a"]


def test_is_valid():
    print()
    day._Day__rules = {
        "0": '"a"',
    }
    assert day.is_valid("a") == True
    assert day.is_valid("b") == False

    day._Day__rules = {
        "0": '"b"',
    }
    assert day.is_valid("b") == True

    day._Day__rules = {
        "0": "1",
        "1": '"a"',
    }
    assert day.is_valid("a") == True
    assert day.is_valid("b") == False

    day._Day__rules = {
        "0": '"b" 1',
        "1": '"a"',
    }
    assert day.is_valid("b") == False
    assert day.is_valid("ba") == True
    assert day.is_valid("bb") == False
    assert day.is_valid("bba") == False

    day._Day__rules = {
        "0": '"a" | "b"',
    }
    assert day.is_valid("a") == True
    assert day.is_valid("b") == True

    day._Day__rules = {
        "0": "4 1 5",
        "1": "4 5",
        "4": '"a"',
        "5": '"b"',
    }
    assert day.is_valid("a") == False
    assert day.is_valid("b") == False
    assert day.is_valid("ab") == False
    assert day.is_valid("aabb") == True
    assert day.is_valid("aaab") == False
    assert day.is_valid("abbb") == False

    day._Day__rules = {
        "0": "4 1 5",
        "1": "2 3",
        "2": "4 4",
        "3": "4 5",
        "4": '"a"',
        "5": '"b"',
    }

    assert day.is_valid("aaaabb") == True

    day._Day__rules = {
        "0": '4 1 5 "c"',
        "1": "2 3 | 3 2",
        "2": "4 4 | 5 5",
        "3": "4 5 | 5 4",
        "4": '"a"',
        "5": '"b"',
    }

    assert day.is_valid("ababbbc") == True
    assert day.is_valid("bababac") == False
    assert day.is_valid("abbbabc") == True
    assert day.is_valid("aaabbbc") == False
    assert day.is_valid("aaaabbbc") == False


def test_calculate_1():
    print()
    day._input_data = [
        "0: 4 1 5",
        "1: 2 3",
        "2: 4 4",
        "3: 4 5",
        '4: "a"',
        '5: "b"',
        "",
        "aaaabb",
        "aaaabb",
    ]
    day._preprocess_input()
    assert day._calculate_1() == 2

    day._input_data = [
        "0: 4 1 5",
        "1: 2 3 | 3 2",
        "2: 4 4 | 5 5",
        "3: 4 5 | 5 4",
        '4: "a"',
        '5: "b"',
        "",
        "ababbb",
        "bababa",
        "abbbab",
        "aaabbb",
        "aaaabbb",
    ]
    assert day._calculate_1() == 2


def test_calculate_2_logic1():
    return
    print()
    day._Day__input = [
        "42: 9 14 | 10 1",
        "9: 14 27 | 1 26",
        "10: 23 14 | 28 1",
        '1: "a"',
        "11: 42 31",
        "5: 1 14 | 15 1",
        "19: 14 1 | 14 14",
        "12: 24 14 | 19 1",
        "16: 15 1 | 14 14",
        "31: 14 17 | 1 13",
        "6: 14 14 | 1 14",
        "2: 1 24 | 14 4",
        "0: 8 11",
        "13: 14 3 | 1 12",
        "15: 1 | 14",
        "17: 14 2 | 1 7",
        "23: 25 1 | 22 14",
        "28: 16 1",
        "4: 1 1",
        "20: 14 14 | 1 15",
        "3: 5 14 | 16 1",
        "27: 1 6 | 14 18",
        '14: "b"',
        "21: 14 1 | 1 14",
        "25: 1 1 | 1 14",
        "22: 14 14",
        "8: 42",
        "26: 14 22 | 1 20",
        "18: 15 15",
        "7: 14 5 | 1 21",
        "24: 14 1",
        "",
        "abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa",
        "bbabbbbaabaabba",
        "babbbbaabbbbbabbbbbbaabaaabaaa",
        "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
        "bbbbbbbaaaabbbbaaabbabaaa",
        "bbbababbbbaaaaaaaabbababaaababaabab",
        "ababaaaaaabaaab",
        "ababaaaaabbbaba",
        "baabbaaaabbaaaababbaababb",
        "abbbbabbbbaaaababbbbbbaaaababb",
        "aaaaabbaabaaaaababaa",
        "aaaabbaaaabbaaa",
        "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
        "babaaabbbaaabaababbaabababaaab",
        "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba",
    ]
    assert day._calculate_1() == 3


def test_calculate_2_easy():
    return
    print()
    day._Day__input = [
        "0: 8",
        '1: "a"',
        "6: 14 14 | 1 14",
        "8: 42",
        "9: 14 27 | 1 26",
        "10: 23 14 | 28 1",
        '14: "b"',
        "15: 1 | 14",
        "16: 15 1 | 14 14",
        "18: 15 15",
        "20: 14 14 | 1 15",
        "22: 14 14",
        "23: 25 1 | 22 14",
        "25: 1 1 | 1 14",
        "26: 14 22 | 1 20",
        "27: 1 6 | 14 18",
        "28: 16 1",
        "42: 9 14 | 10 1",
        "11: 42 31",
        "",
        "a",
        "aa",
        "aaa",
        "aaaa",
        "aaaaa",
        "aaaaaa",
        "b",
    ]
    assert day._calculate_2() == 2


def test_calculate_2():
    return
    print()
    day._Day__input = [
        "42: 9 14 | 10 1",
        "9: 14 27 | 1 26",
        "10: 23 14 | 28 1",
        '1: "a"',
        "11: 42 31",
        "5: 1 14 | 15 1",
        "19: 14 1 | 14 14",
        "12: 24 14 | 19 1",
        "16: 15 1 | 14 14",
        "31: 14 17 | 1 13",
        "6: 14 14 | 1 14",
        "2: 1 24 | 14 4",
        "0: 8 11",
        "13: 14 3 | 1 12",
        "15: 1 | 14",
        "17: 14 2 | 1 7",
        "23: 25 1 | 22 14",
        "28: 16 1",
        "4: 1 1",
        "20: 14 14 | 1 15",
        "3: 5 14 | 16 1",
        "27: 1 6 | 14 18",
        '14: "b"',
        "21: 14 1 | 1 14",
        "25: 1 1 | 1 14",
        "22: 14 14",
        "8: 42",
        "26: 14 22 | 1 20",
        "18: 15 15",
        "7: 14 5 | 1 21",
        "24: 14 1",
        "",
        "abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa",
        "bbabbbbaabaabba",  # original
        "babbbbaabbbbbabbbbbbaabaaabaaa",  # v
        "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",  # v
        "bbbbbbbaaaabbbbaaabbabaaa",  # v
        "bbbababbbbaaaaaaaabbababaaababaabab",  # v
        "ababaaaaaabaaab",  # original
        "ababaaaaabbbaba",  # original
        "baabbaaaabbaaaababbaababb",  # v
        "abbbbabbbbaaaababbbbbbaaaababb",  # v
        "aaaaabbaabaaaaababaa",  # v
        "aaaabbaaaabbaaa",
        "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",  # v
        "babaaabbbaaabaababbaabababaaab",
        "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba",  # v
    ]
    # assert day._calculate_2() == 1
    assert day._calculate_2() == 12
