from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.grid import Grid


@dataclass
class Rotation:
    direction: str
    degrees: int


@dataclass
class Row:
    original: str
    processed: Optional[Rotation] = None

    def __post_init__(self) -> None:
        self.processed = Rotation(*(self.original[0], int(self.original[1:])))


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)
        self.__dir = {"L": -1, "R": 1}

    def _preprocess_input(self):
        self.__input_data = [Row(i) for j in self._input_data for i in j]

    def _calculate_1(self):
        result = 0
        dial = 50
        for x in self.__input_data:
            dial = (
                dial + self.__dir[x.processed.direction] * x.processed.degrees
            ) % 100
            if dial == 0:
                result += 1
        return result

    def _calculate_2(self):
        """Uses brute force after capping the number of rotations"""
        result = 0
        dial = 50
        for x in self.__input_data:
            times = x.processed.degrees // 100
            result += times
            for _ in range(0, x.processed.degrees % 100):
                dial += self.__dir[x.processed.direction]
                dial %= 100
                if dial == 0:
                    result += 1
        return result
