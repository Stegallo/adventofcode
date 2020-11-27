from y_2015.day4 import calculate_1, calculate_2


def test_calculate_1():
    assert calculate_1("abcdef") == 609043
    assert calculate_1("pqrstuv") == 1048970


#
# def test_calculate_2():
#     assert calculate_2("^v") == 3
#     assert calculate_2("^>v<") == 3
#     assert calculate_2("^v^v^v^v^v") == 11
