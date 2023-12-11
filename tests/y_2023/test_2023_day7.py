from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2023.day7 import Day, Hand

with patch("builtins.open", mock_open(read_data="0")):
    day = Day()

def test_Hand():
    print()
    h = Hand('32T3K')
    h = Hand('3333K')
    print(h)
    print(h.rate())
    assert True

def test_Hand_five():
    h = Hand('AAAAA')
    assert h.rate() == ('Five of a kind','A')

def test_Hand_four():
    h = Hand('AA8AA')
    assert h.rate() == ('Four of a kind','A')

def test_Hand_full():
    h = Hand('23332')
    assert h.rate() == ('Full house','3','2')

def test_Hand_three():
    h = Hand('AA8A9')
    assert h.rate() == ('Three of a kind','A')

def test_Hand_two_pair():
    h = Hand('AA898')
    assert h.rate() == ('Two pair','A','8')

def test_Hand_one_pair():
    h = Hand('AA8J9')
    assert h.rate() == ('One pair','A')

def test_Hand_high_card():
    h = Hand('23456')
    assert h.rate() == ('High card', None)

def test__preprocess_input():
    assert True


def test_calculate_1():
    assert True

def test_calculate_2():
    assert True
