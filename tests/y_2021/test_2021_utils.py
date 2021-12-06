from y_2021.utils import decimal_from_binary


def test_decimal_from_binary():
    assert decimal_from_binary([]) == 0
    assert decimal_from_binary([0]) == 0
    assert decimal_from_binary([1]) == 1
    assert decimal_from_binary([1, 0]) == 2
    assert decimal_from_binary([1, 1, 0]) == 6
    assert decimal_from_binary([1, 1, 1]) == 7
