import argparse
import importlib


def load_input(day):
    with open(f"y_2020/input_day{day}.txt") as f:
        x = (f.read()).split("\n")
        if x[-1] == "":
            del x[-1]
    return x


def main():
    """"""
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, help="day as a number")
    args = parser.parse_args()

    x = load_input(args.day)

    day = importlib.import_module(f".day{args.day}", package="y_2020")

    print(f"sol 1: {day.calculate_1(x)}")
    print(f"sol 2: {day.calculate_2(x)}")


if __name__ == "__main__":
    main()
