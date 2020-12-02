from y_2020.day2 import calculate_1, calculate_2


def test_calculate_1():
    assert (
        calculate_1(
            [
                "1-3 a: abcde",
                "1-3 b: cdefg",
                "2-9 c: ccccccccc",
            ]
        )
        == 2
    )


def test_calculate_2():
    assert (
        calculate_2(
            [
                "1-3 a: abcde",
                "1-3 b: cdefg",
                "2-9 c: ccccccccc",
            ]
        )
        == 1
    )
