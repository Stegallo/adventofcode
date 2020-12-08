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
        "light#red": BagRule(
            rules=[{"bright#white": 1}, {"muted#yellow": 2}], cache={}, extension={}
        ),
        "dark#orange": BagRule(
            rules=[{"bright#white": 3}, {"muted#yellow": 4}], cache={}, extension={}
        ),
        "bright#white": BagRule(rules=[{"shiny#gold": 1}], cache={}, extension={}),
        "muted#yellow": BagRule(
            rules=[{"shiny#gold": 2}, {"faded#blue": 9}], cache={}, extension={}
        ),
        "shiny#gold": BagRule(
            rules=[{"dark#olive": 1}, {"vibrant#plum": 2}], cache={}, extension={}
        ),
        "dark#olive": BagRule(
            rules=[{"faded#blue": 3}, {"dotted#black": 4}], cache={}, extension={}
        ),
        "vibrant#plum": BagRule(
            rules=[{"faded#blue": 5}, {"dotted#black": 6}], cache={}, extension={}
        ),
        "faded#blue": BagRule(rules=[{"no#other": 0}], cache={}, extension={}),
        "dotted#black": BagRule(rules=[{"no#other": 0}], cache={}, extension={}),
        "no#other": BagRule(rules=[], cache={}, extension={}),
    }


def test_calculate_1():
    day._Day__rules = {
        "light#red": BagRule(
            rules=[{"bright#white": 1}, {"muted#yellow": 2}], cache={}, extension={}
        ),
        "dark#orange": BagRule(
            rules=[{"bright#white": 3}, {"muted#yellow": 4}], cache={}, extension={}
        ),
        "bright#white": BagRule(rules=[{"shiny#gold": 1}], cache={}, extension={}),
        "muted#yellow": BagRule(
            rules=[{"shiny#gold": 2}, {"faded#blue": 9}], cache={}, extension={}
        ),
        "shiny#gold": BagRule(
            rules=[{"dark#olive": 1}, {"vibrant#plum": 2}], cache={}, extension={}
        ),
        "dark#olive": BagRule(
            rules=[{"faded#blue": 3}, {"dotted#black": 4}], cache={}, extension={}
        ),
        "vibrant#plum": BagRule(
            rules=[{"faded#blue": 5}, {"dotted#black": 6}], cache={}, extension={}
        ),
        "faded#blue": BagRule(rules=[{"no#other": 0}], cache={}, extension={}),
        "dotted#black": BagRule(rules=[{"no#other": 0}], cache={}, extension={}),
        "no#other": BagRule(rules=[], cache={}, extension={}),
    }
    assert day._calculate_1() == 4


def test_calculate_2():
    day._Day__rules = {
        "shiny#gold": BagRule(
            rules=[{"dark#olive": 1}, {"vibrant#plum": 2}], cache={}, extension={}
        ),
        "dark#olive": BagRule(
            rules=[{"faded#blue": 3}, {"dotted#black": 4}], cache={}, extension={}
        ),
        "vibrant#plum": BagRule(
            rules=[{"faded#blue": 5}, {"dotted#black": 6}], cache={}, extension={}
        ),
        "faded#blue": BagRule(rules=[{"no#other": 0}], cache={}, extension={}),
        "dotted#black": BagRule(rules=[{"no#other": 0}], cache={}, extension={}),
        "no#other": BagRule(rules=[], cache={}, extension={}),
    }
    assert day._calculate_2() == 32
