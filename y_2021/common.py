import argparse
import importlib
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, List, Optional


class StopWatch:
    def __init__(self) -> None:
        self.__start_time: Optional[datetime] = None

    def start(self) -> None:
        self.__start_time = datetime.now()

    def lap(self) -> Any:
        return datetime.now() - self.__start_time

    def stop(self) -> Any:
        return datetime.now() - self.__start_time


class AoCDay(ABC):
    """
    Abstract class Day
    """

    @abstractmethod
    def __init__(self, day: int, test: int) -> None:
        self._input_data = load_input(day, test)
        self._preprocess_input()
        self.__stop_watch = StopWatch()

    @abstractmethod
    def _preprocess_input(self) -> None:
        """
        preprocessing of the input
        """

    @abstractmethod
    def _calculate_1(self) -> int:
        """
        _calculate_1
        """

    @abstractmethod
    def _calculate_2(self) -> int:
        """
        _calculate_2
        """

    def solve(self) -> None:
        self.__stop_watch.start()
        print(f"sol 1: {self._calculate_1()} Time taken: {self.__stop_watch.lap()}")

        print(f"sol 2: {self._calculate_2()} Time taken: {self.__stop_watch.stop()}")


def load_input(day: int, test: int) -> List:
    file_name = f"y_2021/input_day{day}{'_test'if test else ''}.txt"
    with open(file_name) as f:
        x = (f.read()).split("\n")
        if x[-1] == "":
            del x[-1]
    return x


def main() -> None:
    """"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int, help="day as a number")
    parser.add_argument("--test", type=int, help="test flag")
    args = parser.parse_args()

    module = importlib.import_module(f"y_2021.day{args.day}")

    day = getattr(module, "Day")(test=args.test)
    day.solve()


if __name__ == "__main__":
    main()
