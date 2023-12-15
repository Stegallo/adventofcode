from common.utilities import Grid, bitand, bitnot, bitor, lshift, rshift


def test_bit_ops():
    assert bitand(1, 2) == 0
    assert bitor(1, 2) == 3
    assert lshift(1, 2) == 4
    assert rshift(1, 2) == 0
    assert bitnot(1) == 65534


def test_grid():
    g = Grid(["ab", "cd"])

    assert g.rows == ["ab", "cd"]
    assert g.cols == ["ac", "bd"]

    assert g.__hash__() == g.__hash__()

    g1 = Grid(["ab", "cd"])
    assert g1.__hash__() == g.__hash__()

    g2 = Grid(["ab", "ef"])
    assert g2.rows == ["ab", "ef"]
    assert g2.cols == ["ae", "bf"]
    assert g1.__hash__() != g2.__hash__()
