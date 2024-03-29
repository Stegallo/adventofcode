from typing import List

from common.aoc import AoCDay

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
    def replace_word_with_number(input: str) -> str:
        for c, k in enumerate(SPELLED):
            input = input.replace(k, k + str(c + 1) + k)
        return input

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
        new_input = [self.replace_word_with_number(i) for i in self.__input_data]
        return self.calculate_calibration(new_input)
