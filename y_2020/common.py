from abc import ABC, abstractmethod
import argparse
import importlib


class AoCDay(ABC):
    """
    Abstract class Day
    """

    @abstractmethod
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

    module = importlib.import_module(f"y_2020.day{args.day}")
    day = getattr(module, f"Day")()
    day.solve()


if __name__ == "__main__":
    main()
