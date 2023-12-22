from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2023.day19 import Day, Branch, ElseBranch, Rule, Interval, State
import copy

with patch("builtins.open", mock_open(read_data="px{a<2006:qkq,m>2090:A,rfg}\n\n{x=787,m=2655,a=1222,s=2876}")):
    day = Day()

# python -m pytest tests/y_2023/test_2023_day19.py::test_process_rule -vvs
def test_rule():
    print()
    rule = Rule.from_input('px{a<2006:qkq,m>2090:A,rfg}')
    print(f"{rule=}")
    # assert False

def test_branch():
    return
    print()
    branch = Branch.from_input('a<2006:A')
    assert branch.combinations()==1
    branch = Branch.from_input('a<2006:R')
    assert branch.combinations()==0
    branch = Branch.from_input('a<2006:qkq')
    print(f"{branch=}")
    print(f"{branch.combinations()=}")
    assert branch.combinations() is None

def test_branch():
    print()
    branch = Branch.from_input('a<2000:A')
    result = branch.intervals(Interval(1,4001))
    assert sum(i.len for i in result) == 4000
    assert result == [Interval(1,2000), Interval(2000,4001)]

    branch = Branch.from_input('a>2000:A')
    result = branch.intervals(Interval(1,4001))
    assert sum(i.len for i in result) == 4000
    assert result == [Interval(2001,4001), Interval(1,2001)]


def test_interval_split():
    i = Interval(1,4001)
    res = i.split(2001)
    assert res == [Interval(1,2001), Interval(2001, 4001)]
    assert i.len == sum(r.len for r in res)

def test_state_apply_final_rules():
    print()
    s = State({})
    result = s.apply(Rule.from_input('end{A}'))
    assert result == 1

    result = s.apply(Rule.from_input('end{R}'))
    assert result == 0

    # result = s.apply(Rule.from_input('end{ii}'))
    # assert result == 0
def test_state_apply():
    # return
    print()
    # s = State({
    # 's':Interval(1, 4001),
    # })
    # result = s.apply(
    # Rule.from_input('in{s<1351:A,R}'),
    # {'A':Rule.from_input('A{A}'),
    #  'R':Rule.from_input('R{R}')},
    # )
    # assert result == 1350
    #
    # s = State({
    # 's':Interval(1, 4001),
    # })
    # result = s.apply(
    # Rule.from_input('in{s<1351:R,R}'),
    # {'A':Rule.from_input('A{A}'),
    #  'R':Rule.from_input('R{R}')},
    # )
    # assert result == 0

    s = State({
    'a':Interval(1, 4001),
    })
    result = s.apply(
    Rule.from_input('fnb{a<345:R,a<547:dgv,a<670:nrm,A}'),
    {'A':Rule.from_input('A{A}'),
     'R':Rule.from_input('R{R}'),
     'dgv':Rule.from_input('dgv{R}'),
     'nrm':Rule.from_input('nrm{R}'),},
    )
    assert result == 3331

def test_state_apply_same_var():
    print()
    s = State({
    'a':Interval(1, 4001),
    })
    result = s.apply(
    Rule.from_input('fnb{a<345:R,A}'),
    {'A':Rule.from_input('A{A}'),
     'R':Rule.from_input('R{R}'),},
    )
    assert result == 3656

    s = State({
    'a':Interval(1, 4001),
    })
    result = s.apply(
    Rule.from_input('fnb{a<345:R,a<547:dgv,a<670:nrm,A}'),
    {'A':Rule.from_input('A{A}'),
     'R':Rule.from_input('R{R}'),
     'dgv':Rule.from_input('dgv{A}'),
     'nrm':Rule.from_input('nrm{A}'),},
    )
    assert result == 3656

    # in{s<1351:px,m>2478:px,x>478:px,a>1478:px,qqz}
    # result = s.apply(Rule.from_input('end{A}'))

def test_get_possible():
    # day.rules={}
    # result = day.get_possibile(Rule.from_input('px{a<4000:A,R}'), {'a':Interval(1,4001)})
    # # assert result == True
    # assert result == {'a':Interval(start=1, end=4000)}
    # day.rules={}
    # result = day.get_possibile(Rule.from_input('px{a<4000:R,A}'), {'a':Interval(1,4001)})
    # # assert result == True
    # assert result == {'a':Interval(start=4000, end=4001)}
    # day.rules={'ff': Rule.from_input('ff{a>3000:R,A}')}
    # result = day.get_possibile(Rule.from_input('px{a<2000:R,ff}'), {'a':Interval(1,4001)})
    # print(result)
    # assert result == {'a': Interval(start=2000, end=3000)}

    day.rules={
    'qqz':Rule.from_input('qqz{s>2770:qs,m<1801:hdj,R}'),
    'qs':Rule.from_input('qs{s>3448:A,lnx}'), 'lnx':Rule.from_input('lnx{m>1548:A,A}'),
    'px':Rule.from_input('px{a<2006:qkq,m>2090:A,rfg}') }
    result = day.get_possibile(Rule.from_input('in{s<1351:px,qqz}'), {'x':Interval(1, 4001),
     'm':Interval(1, 4001),
     'a':Interval(1, 4001),
     's':Interval(1, 4001)})
    assert result == True

def test__preprocess_input():
    assert True


def test_calculate_1():
    assert True


def test_calculate_2():
    assert True
