from y_2015.day5 import calculate_1, calculate_2, twiced, repeated


def test_calculate_1():
    assert calculate_1("ugknbfddgicrmopn") == 1
    assert calculate_1("aaa") == 1
    assert calculate_1("jchzalrnumimnmhp") == 0
    assert calculate_1("haegwjzuvuyypxyu") == 0
    assert calculate_1("dvszwmarrgswjxmb") == 0


def test_twiced():
    assert twiced("xyxy") is True
    assert twiced("aabcdefgaa") is True
    assert twiced("aaa") is False
    assert twiced("aaaa") is True


def test_repeated():
    assert repeated("xyx") is True
    assert repeated("abcdefeghi") is True
    assert repeated("aaa") is True


def test_calculate_2():
    assert calculate_2("qjhvhtzxzqqjkmpb") == 1
    assert calculate_2("xxyxx") == 1
    assert repeated("aaaa") == 1
    assert calculate_2("uurcxstgmygtbstg") == 0
    assert calculate_2("ieodomkazucvgmuy") == 0
