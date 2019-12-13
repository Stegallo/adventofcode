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
