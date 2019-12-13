from unittest.mock import patch
from utils import load_input
from common import run_get_code


def calculate_1(program):
    return run_get_code(program, "day2")[0]


def calculate_2(program):
    for i in range(100):
        for j in range(100):
            program[1] = i
            program[2] = j
            result = calculate_1(program)
            if result == 19690720:
                return i * 100 + j


def main():
    program = load_input()
    res_1 = calculate_1(program)
    res_2 = calculate_2(program)

    print(f"sol 1: {res_1}")
    print(f"sol 2: {res_2}")


if __name__ == "__main__":
    main()


def test_run_get_code():
    """
        tests transformation of the code in the list
    """
    assert run_get_code([1, 0, 0, 0, 99], "day2") == [2, 0, 0, 0, 99]
    assert run_get_code([2, 3, 0, 3, 99], "day2") == [2, 3, 0, 6, 99]
    assert run_get_code([2, 4, 4, 5, 99, 0], "day2") == [2, 4, 4, 5, 99, 9801]
    # fmt: off
    assert run_get_code([1, 1, 1, 4, 99, 5, 6, 0, 99], "day2") \
                    == [30, 1, 1, 4, 2,  5, 6, 0, 99]
    # fmt: on


def test_calculate_1():
    """
        tests extraction of first element from the list after code is run
    """
    assert calculate_1([99]) == 99
    assert calculate_1([1, 0, 0, 0, 99]) == 2


def test_calculate_2_0():
    """
        test the code covering all the combinations
    """

    def mock_calculate_1(l):
        if l[1] == 0 and l[2] == 0:
            return 19690720

    with patch("day2.calculate_1", mock_calculate_1):
        assert calculate_2([1, 0, 0, 0, 99]) == 0


def test_calculate_2_99():
    """
        test the code covering all the combinations
    """

    def mock_calculate_1(l):
        if l[1] == 99 and l[2] == 99:
            return 19690720

    with patch("day2.calculate_1", mock_calculate_1):
        assert calculate_2([1, 0, 0, 0, 99]) == 9999


def test_calculate_2_25():
    """
        test the code covering all the combinations
    """

    def mock_calculate_1(l):
        if l[1] == 25 and l[2] == 75:
            return 19690720

    with patch("day2.calculate_1", mock_calculate_1):
        assert calculate_2([1, 0, 0, 0, 99]) == 2575


def test_calculate_2_75():
    """
        test combination not found
    """
    with patch("day2.calculate_1", lambda x: 0):
        assert calculate_2([1, 0, 0, 0, 99]) == None
