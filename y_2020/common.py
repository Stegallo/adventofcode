import argparse
import importlib
import requests
from abc import ABC, abstractmethod
from datetime import datetime
import os

YEAR = 2020
URL = "https://adventofcode.com/{:d}/day/{:d}/{:s}"


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


def log(msg):
    print(msg)


def load_input(day):

    session = requests.Session()
    log(f"Getting input for year 2020 day {day}... ")

    file_name = f"y_2020/input_day{day}.txt"
    if not os.path.isfile(file_name):

        with open("session_cookie") as f:
            cookie = f.read().rstrip()
            session.cookies.set("session", cookie)

        if not session:
            log("err!\n")
            log("ERROR: cannot download input file without session cookie!\n")
            sys.exit(1)

        log("downloading... ")

        r = session.get(URL.format(YEAR, day, "input"))

        with open(file_name, "wb") as f:
            f.write(r.content)

    with open(file_name) as f:
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

    day = getattr(module, "Day")()
    day.solve()


if __name__ == "__main__":
    main()
