from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.grid import Grid


@dataclass
class Range:
    start: int
    end: int


@dataclass
class Ranges:
    original: str
    processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = Range(*self.original.split("-"))


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [chunk for chunk in self._input_data[0][0].split(",")]
        self.__input_data = [Ranges(j) for j in self.__input_data]

    def _calculate_1(self):
        result = 0
        for x in self.__input_data:
            for y in range(x.processed.start, x.processed.end + 1):
                if len(str(y)) % 2 == 0:
                    left = str(y)[: len(str(y)) // 2]
                    right = str(y)[len(str(y)) // 2 :]
                    if left == right:
                        result += int(y)

        return result

    def _calculate_2(self):
        result = 0
        for x in self.__input_data:
            for y in range(x.processed.start, x.processed.end + 1):
                for y_len in range(1, len(str(y))):
                    subs = str(y)[0:y_len]
                    if len(str(y)) % len(subs) == 0:
                        times = len(str(y)) // len(subs)
                        if subs * times == str(y):
                            result += int(y)
                            break
        return result
