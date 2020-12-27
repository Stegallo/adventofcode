from unittest.mock import mock_open, patch
from collections import defaultdict
from y_2020.day19 import Day

with patch("builtins.open", mock_open(read_data="0: 0")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = ["0: 0", "", "a"]
    day._preprocess_input()
    assert day._Day__rules == {"0": '0 "c"'}
    assert day._Day__messages == ["a"]


def reset_n_assert(day, msg):
    day.cache = defaultdict(dict)
    return day.is_valid(msg)


def test_is_valid():
    print()
    day._Day__rules = {
        "0": '"a"',
    }
    assert reset_n_assert(day, "a") == True
    assert reset_n_assert(day, "b") == False

    day._Day__rules = {
        "0": '"b"',
    }
    assert reset_n_assert(day, "b") == True

    day._Day__rules = {
        "0": "11",
        "11": '"a"',
    }
    assert reset_n_assert(day, "a") == True
    assert reset_n_assert(day, "b") == False

    day._Day__rules = {
        "0": '"b" 1',
        "1": '"a"',
    }
    assert reset_n_assert(day, "b") == False
    assert reset_n_assert(day, "ba") == True
    assert reset_n_assert(day, "bb") == False
    assert reset_n_assert(day, "bba") == False

    day._Day__rules = {
        "0": '"a" | "b"',
    }
    assert reset_n_assert(day, "a") == True
    assert reset_n_assert(day, "b") == True

    day._Day__rules = {
        "0": "4 1 5",
        "1": "4 5",
        "4": '"a"',
        "5": '"b"',
    }
    assert reset_n_assert(day, "a") == False
    assert reset_n_assert(day, "b") == False
    assert reset_n_assert(day, "ab") == False
    assert reset_n_assert(day, "aabb") == True
    assert reset_n_assert(day, "aaab") == False
    assert reset_n_assert(day, "abbb") == False

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
    assert reset_n_assert(day, "ababbbc") == True
    assert reset_n_assert(day, "bababac") == False
    assert reset_n_assert(day, "abbbabc") == True
    assert reset_n_assert(day, "aaabbbc") == False
    assert reset_n_assert(day, "aaaabbbc") == False


def test_is_valid_alternatives():
    day._Day__rules = {
        "0": '4 1 5 "c"',
        "1": "2 3 | 3 2",
        "2": "4 4 | 5 5",
        "3": "4 5 | 5 4",
        # "11": "1 | 2",
        "11": '1 | "b"',
        "4": '"a"',
        "5": '"b"',
    }
    assert reset_n_assert(day, "ababbbc") == True
    # assert reset_n_assert(day, "bababac") == False
    # assert reset_n_assert(day, "abbbabc") == True
    # assert reset_n_assert(day, "aaabbbc") == False
    # assert reset_n_assert(day, "aaaabbbc") == False


def test_calculate_1():
    print()
    day._input_data = [
        '0: 4 1 5 "c"',
        "1: 2 3",
        "2: 4 4",
        "3: 4 5",
        '4: "a"',
        '5: "b"',
        "",
        "aaaabbc",
        "aaaabbc",
    ]
    day._preprocess_input()
    day.cache = defaultdict(dict)
    assert day._calculate_1() == 2

    day._input_data = [
        '0: 4 1 5 "c"',
        "1: 2 3 | 3 2",
        "2: 4 4 | 5 5",
        "3: 4 5 | 5 4",
        '4: "a"',
        '5: "b"',
        "",
        "ababbbc",
        "bababac",
        "abbbabc",
        "aaabbbc",
        "aaaabbbc",
    ]
    day.cache = defaultdict(dict)
    assert day._calculate_1() == 2


def test_is_valid_real():
    print()
    day._Day__rules = {
        "91": "94 94",
        "122": "117 24 | 33 67",
        "6": "117 40 | 33 47",
        "70": "63 33 | 3 117",
        "36": "17 117 | 44 33",
        "111": "33 91 | 117 109",
        "31": "33 69 | 117 41",
        "54": "88 33 | 72 117",
        "52": "33 32 | 117 82",
        "58": "33 43 | 117 122",
        "29": "97 117 | 126 33",
        "129": "51 33 | 7 117",
        "43": "33 35 | 117 97",
        "8": "42",
        "87": "26 33 | 128 117",
        "83": "132 117 | 5 33",
        "57": "126 117",
        "105": "33 2 | 117 64",
        "16": "97 33 | 53 117",
        "110": "33 108 | 117 40",
        "127": "24 117 | 35 33",
        "119": "84 117 | 131 33",
        "135": "109 117 | 126 33",
        "88": "24 33 | 46 117",
        "19": "33 46",
        "64": "117 67 | 33 108",
        "67": "33 117 | 33 33",
        "126": "117 117",
        "12": "43 33 | 50 117",
        "10": "40 33 | 109 117",
        "30": "14 117 | 54 33",
        "108": "33 33 | 117 117",
        "35": "33 94 | 117 117",
        "59": "117 61 | 33 107",
        "93": "50 33 | 76 117",
        "128": "33 40 | 117 53",
        "86": "56 33 | 70 117",
        "115": "33 66 | 117 23",
        "24": "33 117 | 117 94",
        "5": "117 21 | 33 12",
        "79": "33 40 | 117 46",
        "113": "33 30 | 117 75",
        "65": "117 96 | 33 74",
        "1": "91 33 | 24 117",
        "42": "18 33 | 45 117",
        "74": "33 92 | 117 15",
        "56": "129 33 | 101 117",
        "73": "117 35 | 33 85",
        "4": "114 117 | 125 33",
        "63": "68 117 | 111 33",
        "78": "33 108 | 117 91",
        "62": "53 117 | 24 33",
        "98": "109 33 | 85 117",
        "136": "57 33 | 130 117",
        "17": "126 33 | 35 117",
        "7": "108 117 | 53 33",
        "92": "117 109 | 33 67",
        "75": "89 117 | 137 33",
        "104": "33 120 | 117 77",
        "66": "33 37 | 117 103",
        "72": "117 126 | 33 108",
        "106": "117 39 | 33 100",
        "27": "117 60 | 33 1",
        "123": "117 24 | 33 40",
        "82": "124 33 | 76 117",
        "46": "33 33",
        "55": "9 117 | 87 33",
        "100": "40 33 | 35 117",
        "96": "33 116 | 117 38",
        "25": "118 117 | 65 33",
        "89": "22 33 | 102 117",
        "45": "25 117 | 59 33",
        "61": "33 49 | 117 27",
        "109": "94 33 | 33 117",
        "99": "117 33 | 117 117",
        "28": "94 108",
        "40": "117 117 | 33 117",
        "34": "117 46 | 33 53",
        "33": '"a"',
        "130": "47 33 | 40 117",
        "112": "104 117 | 80 33",
        "118": "105 33 | 95 117",
        "69": "117 13 | 33 86",
        "50": "33 40 | 117 67",
        "60": "47 33 | 126 117",
        "101": "84 117 | 123 33",
        "21": "6 33 | 44 117",
        "47": "117 33",
        "84": "33 97 | 117 46",
        "85": "117 33 | 33 117",
        "71": "117 24 | 33 53",
        "80": "106 33 | 93 117",
        "125": "117 99 | 33 109",
        "14": "33 98 | 117 20",
        "107": "136 33 | 48 117",
        "41": "113 117 | 115 33",
        "15": "117 53",
        "9": "33 79 | 117 72",
        "132": "36 33 | 58 117",
        "18": "33 112 | 117 83",
        "133": "33 97",
        "117": '"b"',
        "68": "33 99 | 117 35",
        "49": "110 33 | 62 117",
        "20": "46 117 | 67 33",
        "90": "97 117 | 67 33",
        "134": "117 85 | 33 91",
        "26": "47 33 | 47 117",
        "95": "117 10 | 33 135",
        "103": "121 33 | 73 117",
        "124": "117 126 | 33 91",
        "38": "108 117 | 24 33",
        "53": "117 33 | 33 33",
        "81": "117 53 | 33 91",
        "44": "46 117 | 40 33",
        "114": "33 53 | 117 91",
        "37": "33 16 | 117 90",
        "2": "97 33 | 91 117",
        "97": "33 117",
        "76": "40 33 | 108 117",
        "13": "52 117 | 55 33",
        "39": "35 94",
        "137": "33 133 | 117 134",
        "131": "53 33 | 35 117",
        "22": "33 108 | 117 97",
        "11": "42 31",
        "116": "126 33 | 40 117",
        "32": "78 33 | 81 117",
        "121": "117 91 | 33 46",
        "48": "19 117 | 28 33",
        "102": "108 117 | 99 33",
        "51": "117 67 | 33 46",
        "94": "33 | 117",
        "120": "34 33 | 127 117",
        "23": "33 4 | 117 119",
        "77": "117 62 | 33 71",
        "3": "33 128 | 117 29",
        "0": '8 11 "c"',
    }
    # assert reset_n_assert(day, "abaaaabaabbabbaabbabbbbbbbaabbabaaabbaabc") == False
    assert reset_n_assert(day, "bbbbbbabaaabbbaabaaaaabac") == True
    assert reset_n_assert(day, "babbbabbaabbaaaabbaaaaabbbaabbbbabaabbbac") == False
    assert reset_n_assert(day, "abbbaabbababbaaabaaaaabac") == True


#
# def test_calculate_2_logic1():
#     return
#     print()
#     day._Day__input = [
#         "42: 9 14 | 10 1",
#         "9: 14 27 | 1 26",
#         "10: 23 14 | 28 1",
#         '1: "a"',
#         "11: 42 31",
#         "5: 1 14 | 15 1",
#         "19: 14 1 | 14 14",
#         "12: 24 14 | 19 1",
#         "16: 15 1 | 14 14",
#         "31: 14 17 | 1 13",
#         "6: 14 14 | 1 14",
#         "2: 1 24 | 14 4",
#         "0: 8 11",
#         "13: 14 3 | 1 12",
#         "15: 1 | 14",
#         "17: 14 2 | 1 7",
#         "23: 25 1 | 22 14",
#         "28: 16 1",
#         "4: 1 1",
#         "20: 14 14 | 1 15",
#         "3: 5 14 | 16 1",
#         "27: 1 6 | 14 18",
#         '14: "b"',
#         "21: 14 1 | 1 14",
#         "25: 1 1 | 1 14",
#         "22: 14 14",
#         "8: 42",
#         "26: 14 22 | 1 20",
#         "18: 15 15",
#         "7: 14 5 | 1 21",
#         "24: 14 1",
#         "",
#         "abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa",
#         "bbabbbbaabaabba",
#         "babbbbaabbbbbabbbbbbaabaaabaaa",
#         "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
#         "bbbbbbbaaaabbbbaaabbabaaa",
#         "bbbababbbbaaaaaaaabbababaaababaabab",
#         "ababaaaaaabaaab",
#         "ababaaaaabbbaba",
#         "baabbaaaabbaaaababbaababb",
#         "abbbbabbbbaaaababbbbbbaaaababb",
#         "aaaaabbaabaaaaababaa",
#         "aaaabbaaaabbaaa",
#         "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
#         "babaaabbbaaabaababbaabababaaab",
#         "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba",
#     ]
#     assert day._calculate_1() == 3
#
#
# def test_calculate_2_easy():
#     return
#     print()
#     day._Day__input = [
#         "0: 8",
#         '1: "a"',
#         "6: 14 14 | 1 14",
#         "8: 42",
#         "9: 14 27 | 1 26",
#         "10: 23 14 | 28 1",
#         '14: "b"',
#         "15: 1 | 14",
#         "16: 15 1 | 14 14",
#         "18: 15 15",
#         "20: 14 14 | 1 15",
#         "22: 14 14",
#         "23: 25 1 | 22 14",
#         "25: 1 1 | 1 14",
#         "26: 14 22 | 1 20",
#         "27: 1 6 | 14 18",
#         "28: 16 1",
#         "42: 9 14 | 10 1",
#         "11: 42 31",
#         "",
#         "a",
#         "aa",
#         "aaa",
#         "aaaa",
#         "aaaaa",
#         "aaaaaa",
#         "b",
#     ]
#     assert day._calculate_2() == 2
#
#
# def test_calculate_2():
#     return
#     print()
#     day._Day__input = [
#         "42: 9 14 | 10 1",
#         "9: 14 27 | 1 26",
#         "10: 23 14 | 28 1",
#         '1: "a"',
#         "11: 42 31",
#         "5: 1 14 | 15 1",
#         "19: 14 1 | 14 14",
#         "12: 24 14 | 19 1",
#         "16: 15 1 | 14 14",
#         "31: 14 17 | 1 13",
#         "6: 14 14 | 1 14",
#         "2: 1 24 | 14 4",
#         "0: 8 11",
#         "13: 14 3 | 1 12",
#         "15: 1 | 14",
#         "17: 14 2 | 1 7",
#         "23: 25 1 | 22 14",
#         "28: 16 1",
#         "4: 1 1",
#         "20: 14 14 | 1 15",
#         "3: 5 14 | 16 1",
#         "27: 1 6 | 14 18",
#         '14: "b"',
#         "21: 14 1 | 1 14",
#         "25: 1 1 | 1 14",
#         "22: 14 14",
#         "8: 42",
#         "26: 14 22 | 1 20",
#         "18: 15 15",
#         "7: 14 5 | 1 21",
#         "24: 14 1",
#         "",
#         "abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa",
#         "bbabbbbaabaabba",  # original
#         "babbbbaabbbbbabbbbbbaabaaabaaa",  # v
#         "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",  # v
#         "bbbbbbbaaaabbbbaaabbabaaa",  # v
#         "bbbababbbbaaaaaaaabbababaaababaabab",  # v
#         "ababaaaaaabaaab",  # original
#         "ababaaaaabbbaba",  # original
#         "baabbaaaabbaaaababbaababb",  # v
#         "abbbbabbbbaaaababbbbbbaaaababb",  # v
#         "aaaaabbaabaaaaababaa",  # v
#         "aaaabbaaaabbaaa",
#         "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",  # v
#         "babaaabbbaaabaababbaabababaaab",
#         "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba",  # v
#     ]
#     # assert day._calculate_2() == 1
#     assert day._calculate_2() == 12
