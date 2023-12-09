from common.aoc import AoCDay
from typing import List, Tuple
from collections import defaultdict
from pydantic.dataclasses import dataclass


@dataclass
class Number:
    value: int
    row: int
    start: int
    length: int

    @property
    def border(self) -> List[Tuple[int, int]]:
        return [
            (self.row + y - 1, self.start + x - 1)
            for x in range(self.length + 2)
            for y in range(3)
        ]


def extract_numbers(input, row) -> List[Number]:
    start = 0
    length = 0
    result = []
    for c, i in enumerate(input):
        if i.isnumeric():
            length += 1
        else:
            if length > 0:
                result.append(
                    Number(int(input[start : start + length]), row, start, length),
                )
            start = c + 1
            length = 0
    if length > 0:
        result.append(Number(int(input[start : start + length]), row, start, length))

    return result


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0]
        self.__simbols = {}
        self.__numbers = []
        for c, x in enumerate(self.__input_data):
            for d, y in enumerate(x):
                if y != "." and not y.isnumeric():
                    self.__simbols[(c, d)] = y
            self.__numbers.extend(extract_numbers(x, c))

    def _calculate_1(self) -> int:
        result = 0

        for i in self.__numbers:
            for j in i.border:
                if j in self.__simbols:
                    result += i.value
        return result

    def _calculate_2(self) -> int:
        star_adjacents = defaultdict(list)

        for i in self.__numbers:
            for j in i.border:
                if j in self.__simbols and self.__simbols[j] == "*":
                    star_adjacents[j].append(i.value)
        return sum((v[0] * v[1]) for v in star_adjacents.values() if len(v) == 2)
