from y_2020.utils import collapse_strings, prod


def test_prod():
    assert prod([]) == 1
    assert prod([1]) == 1
    assert prod([2, 3]) == 6


def test_collapse_strings():
    assert collapse_strings(["x", "", "y1", "y2"]) == ["x", "y1 y2"]
    assert collapse_strings(["x", "y", "", "z"]) == ["x y", "z"]
