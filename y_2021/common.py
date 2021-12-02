import argparse
import importlib
from abc import ABC, abstractmethod
from datetime import datetime


class StopWatch:
    def __init__(self):
        self.__start_time = None

    def start(self):
        self.__start_time = datetime.now()

    def lap(self):
        return datetime.now() - self.__start_time

    def stop(self):
        return datetime.now() - self.__start_time


class AoCDay(ABC):
    """
    Abstract class Day
    """

    @abstractmethod
    def __init__(self, day):
        self._input_data = load_input(day)
        self._preprocess_input()
        self.__stop_watch = StopWatch()

    @abstractmethod
    def _preprocess_input(self):
        """
        preprocessing of the input
        """

    @abstractmethod
    def _calculate_1(self):
        """
        _calculate_1
        """

    @abstractmethod
    def _calculate_2(self):
        """
        _calculate_2
        """

    def solve(self):
        self.__stop_watch.start()
        print(f"sol 1: {self._calculate_1()} Time taken: {self.__stop_watch.lap()}")

        print(f"sol 2: {self._calculate_2()} Time taken: {self.__stop_watch.stop()}")


def load_input(day):
    with open(f"y_2021/input_day{day}.txt") as f:
        x = (f.read()).split("\n")
        if x[-1] == "":
            del x[-1]
    return x


def main():
    """"""
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, help="day as a number")
    args = parser.parse_args()

    module = importlib.import_module(f"y_2021.day{args.day}")

    day = getattr(module, "Day")()
    day.solve()


if __name__ == "__main__":
    main()
