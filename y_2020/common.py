from abc import ABC, abstractmethod
import argparse
import importlib


class AoCDay(ABC):
    """
    Abstract class Day
    """

    def __init__(self, day):
        self._input_data = self._preprocess_input(load_input(day))

    @abstractmethod
    def _preprocess_input(self, input_data):
        ...

    @abstractmethod
    def _calculate_1(self):
        ...

    @abstractmethod
    def _calculate_2(self):
        ...

    def solve(self):
        print(f"sol 1: {self._calculate_1()}")
        print(f"sol 2: {self._calculate_2()}")


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

    day = importlib.import_module(f"y_2020.day{args.day}")
    try:
        Day = getattr(day, f"Day{args.day}")
        day = Day(args.day)
        day.solve()
    except AttributeError:
        x = load_input(args.day)
        print(f"sol 1: {day.calculate_1(x)}")
        print(f"sol 2: {day.calculate_2(x)}")


if __name__ == "__main__":
    main()
