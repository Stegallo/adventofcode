from collections import Counter
from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Row:
    original: str
    processed: Optional[list] = None

    def __post_init__(self) -> None:
        self.processed = self.original.split()


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        parsed_input = [Row(i) for i in self._input_data[0]]
        self.__first_list = [int(i.processed[0]) for i in parsed_input]
        self.__second_list = [int(i.processed[1]) for i in parsed_input]

    def _calculate_1(self):
        result = 0
        for x, y in zip(sorted(self.__first_list), sorted(self.__second_list)):
            result += abs(y - x)
        return result

    def _calculate_2(self):
        result = 0
        c = Counter(self.__second_list)
        for x in self.__first_list:
            result += x * c.get(x, 0)
        return result
