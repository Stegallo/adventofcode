from y_2020.utils import prod


def test_prod():
    assert prod([]) == 1
    assert prod([1]) == 1
    assert prod([2, 3]) == 6
