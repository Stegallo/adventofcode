from y_2015.day7 import calculate_1, calculate_2, inner_1, parse


def test_parse():
    assert parse("123 -> x") == ["x", "123"]
    assert parse("x AND y -> z") == ["z", "AND", "x", "y"]
    assert parse("p LSHIFT 2 -> q") == ["q", "LSHIFT", "p", "2"]
    assert parse("NOT e -> f") == ["f", "NOT", "e"]
    assert parse("x OR y -> z") == ["z", "OR", "x", "y"]
    assert parse("p RSHIFT 2 -> q") == ["q", "RSHIFT", "p", "2"]


def test_inner_1():
    assert inner_1(
        [
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i",
        ]
    ) == {
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "x": 123,
        "y": 456,
    }


def test_inner_1_bis():
    assert inner_1(
        [
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i",
            "x AND 456 -> j",
        ]
    ) == {
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "x": 123,
        "y": 456,
        "j": 72,
    }


def test_calculate_1():
    assert (
        calculate_1(
            [
                "123 -> x",
                "456 -> y",
                "x AND y -> d",
                "x OR y -> e",
                "x LSHIFT 2 -> f",
                "y RSHIFT 2 -> g",
                "NOT x -> h",
                "NOT y -> i",
                "1 -> a",
            ]
        )
        == 1
    )


def test_calculate_2():
    assert (
        calculate_2(
            [
                "123 -> x",
                "456 -> y",
                "x AND y -> d",
                "x OR y -> e",
                "x LSHIFT 2 -> f",
                "y RSHIFT 2 -> g",
                "NOT x -> h",
                "NOT y -> i",
                "1 -> a",
                "0 -> b",
            ]
        )
        == 1
    )
