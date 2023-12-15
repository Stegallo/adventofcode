from common.utilities import bitand, bitnot, bitor, lshift, rshift, Grid


def test_bit_ops():
    assert bitand(1, 2) == 0
    assert bitor(1, 2) == 3
    assert lshift(1, 2) == 4
    assert rshift(1, 2) == 0
    assert bitnot(1) == 65534


def test_grid():
    print()
    g = Grid(["ab", "cd"])
    print(g)
    assert g.rows == ["ab", "cd"]
    assert g.cols == ["ac", "bd"]
