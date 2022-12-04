from typing import Set

from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0]

    def __create_set(self, raw_range: str) -> Set:
        range_start, range_end = raw_range.split("-")
        return set(range(int(range_start), int(range_end) + 1))

    def _calculate_1(self):
        def overlaps(s: set, t: set) -> bool:
            return s & t in [s, t]

        return sum(
            1
            for i in self.__input_data
            if overlaps(*(self.__create_set(k) for k in i.split(",")))
        )

    def _calculate_2(self):
        def intersects(s: set, t: set) -> bool:
            return s & t != set()

        return sum(
            1
            for i in self.__input_data
            if intersects(*(self.__create_set(k) for k in i.split(",")))
        )
