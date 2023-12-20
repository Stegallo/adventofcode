from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2023.day19 import Day, process_rule, process_branch
import copy

with patch("builtins.open", mock_open(read_data="px{a<2006:qkq,m>2090:A,rfg}\n\n{x=787,m=2655,a=1222,s=2876}")):
    day = Day()

# python -m pytest tests/y_2023/test_2023_day19.py::test_process_rule -vvs
def test_process_branch():
    print()
    result = process_branch('A', None)
    assert result == None

    result = process_branch('R', None)
    assert result == None

    result = process_branch('a<3000:A', {i:[0, 4000] for i in ('a')})
    # assert result == ({'a': [0, 2999]}, {'a': [2999, 4000]})
    assert result == ({'a': [0, 3000]}, {'a': [3000, 4000]})

    result = process_branch('a<3000:any', {i:[0, 4000] for i in ('a')})
    # assert result == ({'a': [0, 2999]}, {'a': [2999, 4000]})
    assert result == ({'a': [0, 3000]}, {'a': [3000, 4000]})

    result = process_branch('a>3000:any', {i:[0, 4000] for i in ('a')})
    assert result == ({'a': [3000, 4000]}, {'a': [0, 3000]})

def test_process_rule():
    print()
    rule_intervals = {i:[0, 4000] for i in ('x', 'm', 'a', 's')}

    result = process_rule('A'.split(','), {i:[0, 4000] for i in ('a')}, {})
    assert result == {'a': [0, 4000]}

    result = process_rule('a<3000:A,R'.split(','), {i:[0, 4000] for i in ('a')}, {})
    assert result == {'a': [0, 3000]}

    result = process_rule('a>3000:A,R'.split(','), {i:[0, 4000] for i in ('a')}, {})
    assert result == {'a': [3000, 4000]}

    result = process_rule('a<3000:R,A'.split(','), {i:[0, 4000] for i in ('a')}, {})
    assert result == {'a': [3000, 4000]}

    result = process_rule('a>3000:R,A'.split(','), {i:[0, 4000] for i in ('a')}, {})
    assert result == {'a': [0, 3000]}

    result = process_rule('a<3000:A,m<2000:A,R'.split(','), {i:[0, 4000] for i in ('a', 'm')}, {})
    assert result == {'a': [0, 3000], 'm': [0, 2000]}

    result = process_rule('a>3000:A,m>2000:A,R'.split(','), {i:[0, 4000] for i in ('a', 'm')}, {})
    assert result == {'a': [3000, 4000], 'm': [2000, 4000]}

    result = process_rule('a<3000:qqq,R'.split(','), copy.deepcopy(rule_intervals), {'qqq':'A'})
    assert result == {'a': [0, 3000]}

    result = process_rule('a<3000:qqq,zzz'.split(','), copy.deepcopy(rule_intervals), {'qqq':'A', 'zzz':'R'})
    assert result == {'a': [0, 3000]}

    result = process_rule('a<3000:qqq,zzz'.split(','), copy.deepcopy(rule_intervals), {'qqq':'A', 'zzz':'m<2000:A,R'.split(',')})
    assert result == {'a': [0, 3000], 'm': [0, 2000]}

    # result = process_rule('a<2006:qkq,m>2090:A,rfg'.split(','), copy.deepcopy(rule_intervals), {})
    # assert result == 0


def test__preprocess_input():
    assert True


def test_calculate_1():
    assert True


def test_calculate_2():
    assert True
