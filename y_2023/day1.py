from common.aoc import AoCDay
from typing import List

SPELLED = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0]

    @staticmethod
    def calculate_calibration(input: List[str]) -> int:
        s = 0
        for i in input:
            j = [x for x in i if x.isnumeric()]
            s += int(f"{j[0]}{j[-1]}")
        return s

    def _calculate_1(self) -> int:
        return self.calculate_calibration(self.__input_data)

    def _calculate_2(self) -> int:
        new_input = []
        for i in self.__input_data:
            for c, k in enumerate(SPELLED):
                i = i.replace(k, k + str(c + 1) + k)
            new_input.append(i)
        return self.calculate_calibration(new_input)
