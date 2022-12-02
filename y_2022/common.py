import argparse
import importlib
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


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
    def __init__(self, day, test):
        self._input_data = load_input(day, test)
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


def load_input(day, test) -> List[List[str]]:
    file_name = f"y_2022/input_day{day}{'_test'if test else ''}.txt"
    with open(file_name) as f:
        raw_string = f.read()
        if raw_string and raw_string[-1] == "\n":
            raw_string = raw_string[:-1]
        chunks = raw_string.split("\n\n")

    return [k.split("\n") for k in chunks]


def main():
    """"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int, help="day as a number")
    parser.add_argument("--test", type=int, help="test flag")
    args = parser.parse_args()

    module = importlib.import_module(f"y_2022.day{args.day}")

    day = getattr(module, "Day")(test=args.test)
    day.solve()


if __name__ == "__main__":
    main()
