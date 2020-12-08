from unittest.mock import mock_open, patch

from y_2020.day8 import Day, Instruction

with patch("builtins.open", mock_open(read_data=" 0")):
    day = Day()


def test__preprocess_input():
    print()
    day._input_data = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]
    day._preprocess_input()
    assert day._Day__instructions == [
        Instruction(operation="nop", argument=+0),
        Instruction(operation="acc", argument=+1),
        Instruction(operation="jmp", argument=+4),
        Instruction(operation="acc", argument=+3),
        Instruction(operation="jmp", argument=-3),
        Instruction(operation="acc", argument=-99),
        Instruction(operation="acc", argument=+1),
        Instruction(operation="jmp", argument=-4),
        Instruction(operation="acc", argument=+6),
    ]


def test_calculate_1():
    print()
    day._Day__instructions = [
        Instruction(operation="nop", argument=+0),
        Instruction(operation="acc", argument=+1),
        Instruction(operation="jmp", argument=+4),
        Instruction(operation="acc", argument=+3),
        Instruction(operation="jmp", argument=-3),
        Instruction(operation="acc", argument=-99),
        Instruction(operation="acc", argument=+1),
        Instruction(operation="jmp", argument=-4),
        Instruction(operation="acc", argument=+6),
    ]
    assert day._calculate_1() == 5


def test_calculate_2():
    print()
    day._Day__instructions = [
        Instruction(operation="nop", argument=+0),
        Instruction(operation="acc", argument=+1),
        Instruction(operation="jmp", argument=+4),
        Instruction(operation="acc", argument=+3),
        Instruction(operation="jmp", argument=-3),
        Instruction(operation="acc", argument=-99),
        Instruction(operation="acc", argument=+1),
        Instruction(operation="jmp", argument=-4),
        Instruction(operation="acc", argument=+6),
    ]
    assert day._calculate_2() == 8
