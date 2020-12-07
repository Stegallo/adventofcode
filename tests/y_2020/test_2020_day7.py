from unittest.mock import mock_open, patch

from y_2020.day7 import Day, BagRule

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = [
        "light red bags contain 1 bright white bag, 2 muted yellow bags.",
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
        "bright white bags contain 1 shiny gold bag.",
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
        "faded blue bags contain no other bags.",
        "dotted black bags contain no other bags.",
    ]
    day._preprocess_input()
    assert day._Day__rules == {
        "bright#white": BagRule(rules=["shiny#gold"], cache={}),
        "dark#olive": BagRule(rules=["faded#blue", "dotted#black"], cache={}),
        "dark#orange": BagRule(rules=["bright#white", "muted#yellow"], cache={}),
        "dotted#black": BagRule(rules=["no#other"], cache={}),
        "faded#blue": BagRule(rules=["no#other"], cache={}),
        "light#red": BagRule(rules=["bright#white", "muted#yellow"], cache={}),
        "muted#yellow": BagRule(rules=["shiny#gold", "faded#blue"], cache={}),
        "shiny#gold": BagRule(rules=["dark#olive", "vibrant#plum"], cache={}),
        "vibrant#plum": BagRule(rules=["faded#blue", "dotted#black"], cache={}),
        "no#other": BagRule(rules=[], cache={}),
    }


def test_calculate_1_simplified():
    return
    print()
    day._Day__rules = {
        # "bright#white": BagRule(rules=["shiny#gold"], cache={}),
        # "dark#olive": BagRule(rules=["faded#blue", "dotted#black"], cache={}),
        # "dark#orange": BagRule(rules=["bright#white", "muted#yellow"], cache={}),
        "dotted#black": BagRule(rules=["no#other"], cache={}),
        "faded#blue": BagRule(rules=["no#other"], cache={}),
        # "light#red": BagRule(rules=["bright#white", "muted#yellow"], cache={}),
        # "muted#yellow": BagRule(rules=["shiny#gold", "faded#blue"], cache={}),
        # "shiny#gold": BagRule(rules=["dark#olive", "vibrant#plum"], cache={}),
        "vibrant#plum": BagRule(rules=["faded#blue", "dotted#black"], cache={}),
        "no#other": BagRule(rules=[], cache={}),
    }
    assert day._calculate_1() == 4


def test_calculate_1():
    # return
    print()
    day._Day__rules = {
        "bright#white": BagRule(rules=["shiny#gold"], cache={}),
        "dark#olive": BagRule(rules=["faded#blue", "dotted#black"], cache={}),
        "dark#orange": BagRule(rules=["bright#white", "muted#yellow"], cache={}),
        "dotted#black": BagRule(rules=["no#other"], cache={}),
        "faded#blue": BagRule(rules=["no#other"], cache={}),
        "light#red": BagRule(rules=["bright#white", "muted#yellow"], cache={}),
        "muted#yellow": BagRule(rules=["shiny#gold", "faded#blue"], cache={}),
        "shiny#gold": BagRule(rules=["dark#olive", "vibrant#plum"], cache={}),
        "vibrant#plum": BagRule(rules=["faded#blue", "dotted#black"], cache={}),
        "no#other": BagRule(rules=[], cache={}),
    }
    assert day._calculate_1() == 4


#
#
# def test_calculate_2():
#     print()
#     day._Day__input == []
#     assert day._calculate_2() == 0
