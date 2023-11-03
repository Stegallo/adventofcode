import argparse
import importlib
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

from .get_file import pull_file


class AoCDay(ABC):
    """
    Abstract class Day
    """

    @abstractmethod
    def __init__(self, path:str, test: bool):
        day_info = AoCDay.get_day_info(path)
        self._year = day_info.year
        self._day = day_info.day
        self._test = test
        self._input_data = self._load_input()
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

    @staticmethod
    def get_day_info(path:str):
        """
        TODO typehint
        """
        return DayInfo.from_path(path)

    def _load_input(self) -> List[List[str]]:

        raw_string = self._get_file_content()

        if raw_string and raw_string[-1] == "\n":
            raw_string = raw_string[:-1]
        chunks = raw_string.split("\n\n")

        return [k.split("\n") for k in chunks]

    def _get_file_content(self):
        file_name = f"y_{self._year}/input_day{self._day}{'_test'if self._test else ''}.txt"
        try:
            with open(file_name) as f:
                raw_string = f.read()
        except FileNotFoundError:
            pull_file(self._year, self._day)
            with open(file_name) as f:
                raw_string = f.read()
        return raw_string


    def solve(self):
        self.__stop_watch.start()
        print(f"sol 1: {self._calculate_1()} Time taken: {self.__stop_watch.lap()}")

        print(f"sol 2: {self._calculate_2()} Time taken: {self.__stop_watch.stop()}")


class DayInfo():

    year: int
    day: int

    @staticmethod
    def from_path(path: str):
        """
        TODO typehint
        """
        day_info = DayInfo()
        day_info.year = path.split(".")[0].replace("y_", "")
        day_info.day = path.split(".")[1].replace("day", "")
        return day_info


class StopWatch:
    def __init__(self):
        self.__start_time = None

    def start(self):
        self.__start_time = datetime.now()

    def lap(self):
        return datetime.now() - self.__start_time

    def stop(self):
        return datetime.now() - self.__start_time


def main():
    """"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, help="year as a number")
    parser.add_argument("--day", type=int, help="day as a number")
    parser.add_argument("--test", type=int, help="test flag")
    args = parser.parse_args()

    module = importlib.import_module(f"y_{args.year}.day{args.day}")

    day = getattr(module, "Day")(test=args.test)
    day.solve()
