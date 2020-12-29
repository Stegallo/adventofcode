from unittest.mock import mock_open, patch

from y_2020.day21 import Day

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = [
        "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
        "trh fvjkl sbzzf mxmxvkd (contains dairy)",
        "sqjhc fvjkl (contains soy)",
        "sqjhc mxmxvkd sbzzf (contains fish)",
    ]
    day._preprocess_input()
    assert day._Day__recipes == [
        [["mxmxvkd", "kfcds", "sqjhc", "nhms"], ["dairy", "fish"]],
        [["trh", "fvjkl", "sbzzf", "mxmxvkd"], ["dairy"]],
        [["sqjhc", "fvjkl"], ["soy"]],
        [["sqjhc", "mxmxvkd", "sbzzf"], ["fish"]],
    ]
    assert day._Day__possible_allers == {
        "kfcds": {"dairy", "fish"},
        "mxmxvkd": {"dairy", "fish"},
        "nhms": {"dairy", "fish"},
        "sqjhc": {"dairy", "soy", "fish"},
        "trh": {"dairy"},
        "sbzzf": {"dairy", "fish"},
        "fvjkl": {"dairy", "soy"},
    }
    assert day._Day__recipes_with == {"dairy": [0, 1], "fish": [0, 3], "soy": [2]}


def test_calculate_1():
    print()
    day._input_data = [
        "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
        "trh fvjkl sbzzf mxmxvkd (contains dairy)",
        "sqjhc fvjkl (contains soy)",
        "sqjhc mxmxvkd sbzzf (contains fish)",
    ]
    day._preprocess_input()
    assert day._calculate_1() == 5


def test_calculate_2():
    print()
    day._input_data = [
        "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
        "trh fvjkl sbzzf mxmxvkd (contains dairy)",
        "sqjhc fvjkl (contains soy)",
        "sqjhc mxmxvkd sbzzf (contains fish)",
    ]
    day._preprocess_input()
    assert day._calculate_2() == "mxmxvkd,sqjhc,fvjkl"
